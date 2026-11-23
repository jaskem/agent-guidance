from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools.check_learning_change import evaluate

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / 'tools/check_learning_change.py'


def valid_record(kind='guidance_patch'):
    record = {
        'schema_version': 1,
        'id': 'learning-001',
        'kind': kind,
        'owner': 'repository maintainer',
        'authorization_ref': 'task:accepted-scope',
        'scope': 'instructions_only',
        'risk_flags': [],
        'observation': {'effect': 'Wrong route selected', 'evidence': ['trial:before']},
        'baseline': {'ref': 'trial:before', 'outcome': 'fail'},
        'candidate': {'ref': 'trial:after', 'outcome': 'pass'},
        'checks': dict.fromkeys(('positive', 'adjacent_valid', 'excluded',
                                'missing_input', 'regression'), True),
        'review': {'independent': True, 'findings_resolved': True,
                   'evidence': ['review:resolved']},
        'rollback': {'ref': 'revision:previous', 'restore_procedure': 'Restore pinned revision'},
    }
    if kind in ('new_skill', 'upstream_refresh'):
        record['source'] = {
            'url': 'https://example.org/owner/skills', 'commit': 'a' * 40,
            'license': 'MIT', 'all_files_reviewed': True, 'no_unapproved_execution': True,
        }
    if kind == 'new_skill':
        record['novelty'] = {
            'existing_routes_checked': True, 'distinct_outcome': 'Validate signed invoices',
            'adapt_existing_reason': 'No existing route covers invoice signatures',
        }
    return record


def change(record, path, value):
    obj = record
    *parents, key = path.split('.')
    for parent in parents:
        obj = obj[parent]
    obj[key] = value


class LearningChangeTests(unittest.TestCase):
    def assert_decision(self, record, expected):
        result = evaluate(record)
        self.assertEqual(result['decision'], expected, result)
        self.assertIsInstance(result['reasons'], list)
        if expected == 'eligible':
            self.assertEqual(result['reasons'], [])
        else:
            self.assertTrue(result['reasons'])

    def test_supported_changes_can_satisfy_contract(self):
        for kind in ('guidance_patch', 'skill_patch', 'upstream_refresh', 'new_skill', 'rollback'):
            with self.subTest(kind=kind):
                self.assert_decision(valid_record(kind), 'eligible')

    def test_evaluation_does_not_modify_input_or_resolve_refs(self):
        record = valid_record()
        # These are declarations, deliberately not existing files or live URLs.
        record['authorization_ref'] = '/nonexistent/authorization'
        record['review']['evidence'] = ['https://invalid.invalid/review']
        before = deepcopy(record)
        self.assert_decision(record, 'eligible')
        self.assertEqual(record, before)

    def test_all_required_fields_are_required(self):
        record = valid_record()
        paths = ['schema_version', 'id', 'kind', 'owner', 'authorization_ref', 'scope',
                 'risk_flags', 'observation', 'observation.effect', 'observation.evidence',
                 'baseline', 'baseline.ref', 'baseline.outcome', 'candidate', 'candidate.ref',
                 'candidate.outcome', 'checks', 'review', 'review.evidence', 'rollback',
                 'rollback.ref', 'rollback.restore_procedure']
        paths += ['checks.' + key for key in record['checks']]
        paths += ['review.independent', 'review.findings_resolved']
        for path in paths:
            with self.subTest(path=path):
                candidate = deepcopy(record)
                obj = candidate
                *parents, key = path.split('.')
                for parent in parents:
                    obj = obj[parent]
                del obj[key]
                self.assert_decision(candidate, 'blocked')

    def test_bad_root_unknown_actions_and_schema_are_blocked(self):
        for value in (None, [], 'record', 1):
            with self.subTest(root=value):
                self.assert_decision(value, 'blocked')
        for path, value in [('kind', 'install'), ('kind', []), ('schema_version', True),
                            ('schema_version', 1.0), ('schema_version', 2)]:
            with self.subTest(path=path, value=value):
                record = valid_record()
                change(record, path, value)
                self.assert_decision(record, 'blocked')

    def test_malformed_or_empty_evidence_is_blocked(self):
        for path in ('observation.evidence', 'review.evidence'):
            for value in (None, 'trial:one', [], [''], ['  '], [True], [{}]):
                with self.subTest(path=path, value=value):
                    record = valid_record()
                    change(record, path, value)
                    self.assert_decision(record, 'blocked')
        for path in ('observation', 'baseline', 'candidate', 'checks', 'review', 'rollback'):
            for value in (None, [], True):
                with self.subTest(path=path, value=value):
                    record = valid_record()
                    change(record, path, value)
                    self.assert_decision(record, 'blocked')

    def test_text_cannot_be_empty_or_non_text(self):
        for path in ('id', 'owner', 'authorization_ref', 'scope', 'observation.effect',
                     'baseline.ref', 'candidate.ref', 'rollback.ref', 'rollback.restore_procedure'):
            for value in ('', ' \n ', 1, None):
                with self.subTest(path=path, value=value):
                    record = valid_record()
                    change(record, path, value)
                    self.assert_decision(record, 'blocked')

    def test_checks_and_review_require_actual_true(self):
        for path in ('checks.positive', 'checks.adjacent_valid', 'checks.excluded',
                     'checks.missing_input', 'checks.regression', 'review.independent',
                     'review.findings_resolved'):
            for value in (False, 1, 'true', None):
                with self.subTest(path=path, value=value):
                    record = valid_record()
                    change(record, path, value)
                    self.assert_decision(record, 'blocked')

    def test_adjacent_valid_is_required_for_every_change_kind(self):
        for kind in ('guidance_patch', 'skill_patch', 'upstream_refresh', 'new_skill', 'rollback'):
            record = valid_record(kind)
            del record['checks']['adjacent_valid']
            with self.subTest(kind=kind):
                result = evaluate(record)
                self.assertEqual(result['decision'], 'blocked', result)
                self.assertIn('checks.adjacent_valid must be true', result['reasons'])

    def test_failed_or_unknown_candidate_is_never_eligible(self):
        for path, value in [('candidate.outcome', 'fail'), ('candidate.outcome', None),
                            ('baseline.outcome', 'unknown')]:
            with self.subTest(path=path, value=value):
                record = valid_record()
                change(record, path, value)
                self.assert_decision(record, 'blocked')

    def test_pass_to_pass_requires_strict_measurable_benefit(self):
        record = valid_record()
        record['baseline']['outcome'] = 'pass'
        self.assert_decision(record, 'blocked')
        for direction, before, after, expected in (
                ('lower', 10, 8, 'eligible'), ('higher', 8, 10, 'eligible'),
                ('lower', 8, 10, 'blocked'), ('higher', 10, 8, 'blocked'),
                ('lower', 8, 8, 'blocked'), ('higher', 8, 8, 'blocked')):
            with self.subTest(direction=direction, before=before, after=after):
                record['benefit'] = {'metric': 'task duration', 'baseline': before,
                                     'candidate': after, 'direction': direction}
                self.assert_decision(record, expected)

    def test_benefit_rejects_nonfinite_boolean_or_malformed_values(self):
        base = valid_record()
        base['baseline']['outcome'] = 'pass'
        base['benefit'] = {'metric': 'task duration', 'baseline': 10,
                           'candidate': 8, 'direction': 'lower'}
        for path, value in [('benefit', None), ('benefit.metric', ''),
                            ('benefit.direction', 'equal'), ('benefit.baseline', True),
                            ('benefit.candidate', '8'), ('benefit.baseline', float('nan')),
                            ('benefit.candidate', float('inf')),
                            ('benefit.candidate', float('-inf'))]:
            with self.subTest(path=path, value=value):
                record = deepcopy(base)
                change(record, path, value)
                self.assert_decision(record, 'blocked')
        base['benefit']['baseline'] = 10 ** 1000
        self.assert_decision(base, 'eligible')

    def test_risks_and_scope_route_to_manual_review(self):
        record = valid_record()
        record['risk_flags'] = ['external_dependency']
        self.assert_decision(record, 'manual_review')
        record['risk_flags'] = []
        record['scope'] = 'external_writes'
        self.assert_decision(record, 'manual_review')
        del record['review']['evidence']
        self.assert_decision(record, 'blocked')

    def test_prohibited_or_malformed_risks_are_blocked(self):
        for flags in (['approval_bypass'], ['secrets'], ['ignore_user_instructions'],
                      [' SECRETS '], ['external_dependency', 'secrets'],
                      None, {}, 'secrets', [1], ['']):
            with self.subTest(flags=flags):
                record = valid_record()
                record['risk_flags'] = flags
                self.assert_decision(record, 'blocked')

    def test_upstream_and_new_skill_require_reviewed_pinned_source(self):
        cases = [('source', None), ('source.url', 'http://example.org/skills'),
                 ('source.url', 'https:///missing-host'), ('source.url', 'https://host:bad'),
                 ('source.url', 'https://user:secret@example.org/skills'),
                 ('source.url', 'https://example.org/\nhidden'),
                 ('source.url', 'https://example.org/\x00hidden'),
                 ('source.commit', 'latest'), ('source.commit', 'g' * 40),
                 ('source.commit', 'a' * 39), ('source.license', ''),
                 ('source.all_files_reviewed', 1), ('source.no_unapproved_execution', False)]
        for kind in ('upstream_refresh', 'new_skill'):
            for path, value in cases:
                with self.subTest(kind=kind, path=path, value=value):
                    record = valid_record(kind)
                    change(record, path, value)
                    self.assert_decision(record, 'blocked')
            record = valid_record(kind)
            del record['source']
            self.assert_decision(record, 'blocked')

    def test_new_skill_requires_overlap_and_adaptation_assessment(self):
        for path, value in [('novelty', None), ('novelty.existing_routes_checked', False),
                            ('novelty.existing_routes_checked', 1),
                            ('novelty.distinct_outcome', ''),
                            ('novelty.adapt_existing_reason', '')]:
            with self.subTest(path=path, value=value):
                record = valid_record('new_skill')
                change(record, path, value)
                self.assert_decision(record, 'blocked')
        record = valid_record('new_skill')
        del record['novelty']
        self.assert_decision(record, 'blocked')

    def test_rollback_does_not_bypass_evidence_or_recovery_contract(self):
        record = valid_record('rollback')
        record['rollback']['restore_procedure'] = ''
        self.assert_decision(record, 'blocked')
        record = valid_record('rollback')
        record['review']['independent'] = False
        self.assert_decision(record, 'blocked')


class LearningChangeCliTests(unittest.TestCase):
    def run_cli(self, raw):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'record.json'
            path.write_bytes(raw if isinstance(raw, bytes) else raw.encode('utf-8'))
            completed = subprocess.run([sys.executable, str(CHECKER), str(path)],
                                       capture_output=True, text=True, check=False)
        self.assertEqual(completed.stderr, '')
        return completed.returncode, json.loads(completed.stdout)

    def test_adjacent_valid_declaration_controls_cli_decision(self):
        for case in ('missing', 'false', 'true'):
            with self.subTest(case=case):
                record = valid_record()
                if case == 'missing':
                    del record['checks']['adjacent_valid']
                else:
                    record['checks']['adjacent_valid'] = case == 'true'
                code, result = self.run_cli(json.dumps(record))
                if case == 'true':
                    self.assertEqual((code, result), (0, {'decision': 'eligible', 'reasons': []}))
                else:
                    self.assertEqual(code, 1)
                    self.assertEqual(result['decision'], 'blocked')
                    self.assertIn('checks.adjacent_valid must be true', result['reasons'])

    def test_output_and_exit_codes_match_decisions(self):
        for decision, status, update in (
                ('eligible', 0, {}), ('manual_review', 2, {'risk_flags': ['dependency']}),
                ('blocked', 1, {'kind': 'install'})):
            with self.subTest(decision=decision):
                record = valid_record()
                record.update(update)
                code, result = self.run_cli(json.dumps(record))
                self.assertEqual(code, status)
                self.assertEqual(result, evaluate(record))

    def test_invalid_json_duplicates_and_encoding_are_blocked(self):
        for raw in ('{', '[]', '{"id":"one","id":"two"}',
                    json.dumps(valid_record())[:-1] + ',"metadata":NaN}', b'\xff'):
            with self.subTest(raw=raw):
                code, result = self.run_cli(raw)
                self.assertEqual(code, 1)
                self.assertEqual(result['decision'], 'blocked')
                self.assertTrue(result['reasons'])

    def test_missing_file_or_wrong_argument_count_is_json_blocked(self):
        for args in ([], ['a', 'b'], ['/nonexistent/learning-record.json']):
            with self.subTest(args=args):
                completed = subprocess.run([sys.executable, str(CHECKER), *args],
                                           capture_output=True, text=True, check=False)
                self.assertEqual(completed.returncode, 1)
                self.assertEqual(completed.stderr, '')
                self.assertEqual(json.loads(completed.stdout)['decision'], 'blocked')


if __name__ == '__main__':
    unittest.main()

---
name: domain-modeling
description: Clarify or change domain terminology, identity, relationships and invariants using concrete cases. Use for ambiguous concepts or domain-contract design. Exclude merely reading known terms and routine implementation with an established model.
---

# Domain modeling

## 1. Locate the owner

Read the project router, relevant domain/data role and existing glossary, central concept, contract or decision record. Use their actual locations; do not impose a new glossary or ADR directory. Identify whether the current discussion changes meaning or only asks for an explanation.

## 2. Separate concepts using evidence

List the terms causing ambiguity and their current definitions. Distinguish entity identity, display name, source identifier, ordering, representation and lifecycle. Verify statements about implemented behavior against code or data. Mark discrepancies between intended and implemented behavior without silently choosing either as the approved design.

Test the proposed meaning with a normal example, a boundary case and a counterexample. Label invented examples as hypothetical. Ask only about missing domain decisions; inspect facts yourself. Never equate two identifiers merely because current samples happen to match.

## 3. Record the resolved meaning

Use [semantic records](references/semantic-records.md). Capture accepted definitions, relevant invariants and aliases at the existing owner. Keep unresolved meanings proposed. Do not change schemas, rename code or migrate data unless implementation is authorized.

Record a separate decision only when alternatives and the reason for choosing matter to future work. Avoid duplicating existing product decisions. Keep definitions about meaning; implementation details belong in the owning technical document.

## 4. Check use across boundaries

Trace one example through source, normalized model, storage and display as relevant. Check cardinality, units, absent/unknown/error states, identity stability and compatibility. Link any implementation mismatch as a separate follow-up rather than claiming the written model is deployed.

Finish with resolved terms, remaining decision if any and concrete proof cases. Load only roles needed for material risks.

Read [sources and adaptation](references/sources.md) when maintaining this package.

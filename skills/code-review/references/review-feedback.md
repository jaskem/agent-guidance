# Assess feedback before changing code

Read the exact comment, originating requirement, actual baseline and current change. Trace the claimed failure through relevant callers and existing tests. Reproduce a distinguishing case where practical; a review comment is evidence to investigate, not proof of a defect.

Classify each item as supported, unsupported, materially unclear or outside the authorized scope. Give a concrete reason and source for disputed feedback. Keep independently authorized fixes moving when one comment is unclear; pause only its dependent work. Resolve a material product decision with its actual owner instead of adopting a reviewer's preference as a requirement.

Apply supported in-scope fixes through evidence-driven-development, preserve the review's comparison and inspect the complete resulting diff. HEAD~1 is valid only when it is the actual complete requested scope; it can omit earlier commits or uncommitted work. Recheck affected tests and any material changed reasoning after fixes. A green suite does not itself settle every finding.

Keep requirements and quality acceptance separate. A complexity-only pass, maximum number of review rounds or recorded ruling cannot establish an unmet product criterion. Leave the criterion open with its evidence and next action. Send external replies only when communication is authorized; preparing a finding does not authorize posting it.

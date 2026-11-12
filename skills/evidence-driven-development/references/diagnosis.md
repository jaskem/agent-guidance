# Diagnose the reported symptom

1. Pin the failing environment, input and expected result. Inspect enough code and configuration to reach the actual call path. Build the smallest practical repeatable check: existing test, fixture invocation, browser journey, request replay or measurement. Record the command/action and observed failure. For intermittent failures record run counts and reproduction rate; one green run is not a fix.
2. Reduce the scenario while preserving that symptom. Keep the original scenario for final verification. Do not mistake a nearby error or missing dependency for the reported bug.
3. Form plausible competing explanations, each with an observation that could disprove it. Use as many as the evidence warrants; a numerical quota adds noise. Select the cheapest probe that separates them. Reading code is allowed; label untested explanations as hypotheses.
4. Change one relevant variable per probe. For performance use before/after measurements under comparable conditions. Keep credentials and private payloads out of logs and reports.
5. Fix the supported cause and exercise both the reduced case and original scenario. Add a durable regression check at the real boundary if one is available. If the environment cannot reproduce the bug, report exactly what is missing; do not claim causal certainty or successful repair. Continue independent inspection or a clearly labelled provisional change only within authorized scope.
6. Remove temporary instrumentation. Record any missing test boundary as a concrete limitation, not as proof that the symptom is fixed.

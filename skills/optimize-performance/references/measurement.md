# Measurement notes

Before/after evidence needs the same operation and comparable conditions.

Record input identity/size, revision/build, hardware/runtime, important configuration, concurrency, cache state, sample count or fixed time budget, metric and observation method. Keep warm-up separate. Choose repetitions that expose ordinary variation; report the distribution or a justified stable summary rather than the fastest run.

Use the symptom to select a small diagnostic:

- A blocked UI needs event/main-thread or native runtime evidence.
- Slow imports need time by phase on representative files.
- Slow data access needs actual request/query plans and counts.
- Intermittent pauses may require bounded traces of contention, allocation or external waits.
- File-share behavior needs the real intended network/storage boundary before claiming that environment improved.

State the experiment's expected mechanism and disproof condition. Change one cause at a time where practical. Inspect correctness costs of caching, batching, parallelism, skipped work and changed precision; a faster wrong result is a regression.

Compare the effect with run-to-run variation and any accepted target. A result inside noise is inconclusive. Keep a minimal useful attempted-idea record at the existing task/PR owner with before/after evidence and why it was kept or removed. Never report a vendor benchmark or a fixture result as measured user-project gain.

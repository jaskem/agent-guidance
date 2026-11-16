# Signal cases

Read the relevant case when choosing signals or checking ambiguous failure evidence. Keep only signals that answer the task's diagnostic questions.

## A job has several entry points

A scheduled run, manual CLI run and replay endpoint write to one file. Give each run a correlation identifier and an explicit entry point at its origin; carry both into queued work. An identifier groups events but does not establish which entry point started them. Distinguish the logical operation from each retry attempt so three failed attempts followed by success do not appear as three failed jobs.

Validate externally supplied identifiers for format and length. Keep arbitrary input out of metric dimensions and log syntax. Verify concurrent runs remain distinguishable in the emitted output.

## A portable or offline application has no telemetry service

A bounded local event file and a diagnostic export may answer the question. Record relevant application version, operation, outcome and run identity without exposing document contents or full personal paths. Choose rotation, access and export behavior appropriate to the machine and user.

Reproduce a known failed operation and a healthy operation. Use the saved output to identify the failed run and its cause category. Check logging behavior when the directory is unwritable or full: the application should retain its specified behavior and expose a collection gap where feasible. Local proof does not establish central collection or remote alert delivery.

## A metric grows with user traffic

For aggregate rates or latency, use dimensions with bounded values such as operation type and result category. A raw URL, request identifier, customer identifier or exception message creates a new series for each distinct value. Move justified case-level detail into protected, bounded events; omit it when the diagnostic question does not need it.

Estimate series count from the dimension combinations and event volume from expected traffic. Use latency distributions when the question concerns slow-tail behavior; do not claim reliable percentiles from too few observations. Sample with an explicit statement of which rare failures can be missed.

## An alert appears healthy because data is absent

Distinguish successful work, no work, delayed reporting and failed collection. A zero-error query cannot demonstrate health if its denominator or collector is missing. Use a deliberate failure and a healthy control to check the predicate, grouping and evaluation window. Test delivery through a safe sink unless the task already authorizes the real notification.

Base thresholds and duration on an accepted target, baseline or explicit experiment. Include the affected operation, first useful query and existing response owner. Keep resource alarms when they represent an actionable capacity or failure risk; do not assume every metric deserves a page.

## Instrumentation changes the operation

Check sensitive fields in actual output, not just logger arguments. Redaction may miss nested errors or exported spans. Bound buffers, retention and synchronous work, and check what happens when a sink is slow or unavailable. Follow the application's required failure behavior; do not let an optional diagnostic dependency silently become a new product dependency.

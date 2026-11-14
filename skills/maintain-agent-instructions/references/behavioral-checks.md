# Check a changed method

Use raw tasks, inputs and outputs to exercise the method's intended result. Compare an unchanged baseline when it is important to know whether the new wording contributes anything. A plausible improvement is not demonstrated merely because the new run succeeds.

Include a normal request, a request outside the skill's scope and a missing-input or inaccessible-tool case. For selection changes, include nearby skills with similar names and a simple chat that needs no full workflow. Check whether existing consent, task ownership and product acceptance survive the route.

For substantial changes, assign a fresh task-local agent the skill plus a realistic request and raw artifacts. Do not provide the intended answer, suspected defect or prior analysis. Distinguish a true fresh-context run from an agent inheriting the author's diagnosis. Observe the returned result and evidence; a worker saying “passed” is insufficient.

Check autonomous delegation without requiring a user to say “use subagents”: a useful independent task should receive a bounded assignment; a tightly coupled trivial task should not acquire a ceremonial team. Check missing agent capability and shared-object ownership as separate cases.

Use mechanical checks for catalog/package equality, complete local references and invocation metadata; use reasoning cases for behavior. Do not install a vendor's untested floor-check script as if it already enforced the project's requirements. Keep a concrete recurrence case at the existing feedback owner, not a new permanent audit process.

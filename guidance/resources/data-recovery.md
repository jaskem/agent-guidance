# Reasoning about uncertain writes

Optional advisory resource for `domain-data-contracts`, `local-first-sync-recovery`, and `architecture-engineering`. Use when a write's outcome, retry safety, or recovery authority is unresolved. Skip when the accepted contract and existing evidence already answer that question. This is a reasoning aid, not a new persistence protocol or permission to reopen an accepted contract.

## Separate the questions

| Question | Evidence to look for | Insufficient substitute |
| --- | --- | --- |
| What operation was attempted? | Stable operation identity and intended effect | A current screen label |
| Did that operation commit? | Evidence correlated to that operation at the owning boundary | A timeout or a generic success response from a different attempt |
| What is true now? | Current authoritative state under the relevant identity/access rules | Historical completion alone |
| May it be retried? | Defined duplicate handling or authoritative resolution under the existing contract | A new request ID or a reload |

Original hypothetical example: a client submits a stock adjustment and loses the response. The current quantity cannot identify whether that adjustment committed if another writer also changed stock. Retrying with a new identity could duplicate the adjustment. If the service provides a correlated receipt, it may resolve the historical outcome; it does not necessarily prove today's stock level or current permission to write. Without suitable evidence, preserve the uncertainty through the existing recovery contract.

The relevant boundary may be a local transaction, a service operation, or a multi-step workflow. Do not transfer atomicity or durability guarantees between them. For IndexedDB-specific questions, consult the actual transaction lifecycle and durability semantics in the specification and the runtime being used; a successful individual request is not the same claim as a completed transaction.

## Useful counterexamples

- A completed local write does not establish that a separate remote side effect happened.
- A retry key has no protective meaning unless the receiver's scope, retention, and duplicate semantics support it.
- A restored interface can be usable while an earlier mutation remains unresolved.

Select only the counterexample that threatens the present claim. This reference adds no universal locking scheme, event store, retry algorithm, or mandatory failure matrix. Consumer contracts own exact outcomes, blocking, and recovery behavior.

## Sources

Reviewed 2026-09-28. Original synthesis and hypothetical example; no upstream rule set is copied.

- Conceptual community reference: Maciej Ciemborowicz, [DDIA-inspired decision rules](https://github.com/ciembor/agent-rules-books/blob/893a88a6fce3a80c565bf39ac65021b43a8b2990/designing-data-intensive-applications/designing-data-intensive-applications.mini.md). This is an unofficial interpretation inspired by Martin Kleppmann's book, not a runtime specification.
- Primary browser-storage reference: [Indexed Database API 3.0](https://www.w3.org/TR/IndexedDB/), especially transaction lifecycle, commit, and durability. The live specification is not a guarantee of support in every deployed browser.
- Deliberately excluded: the source's whole-system checklist and unrelated replication, partitioning, or stream-processing guidance. Existing repository evidence and relevant primary specifications decide applicability.

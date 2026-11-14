# Task graph and recovery

Maintain one record per task at its existing owner: source requirement, accepted result, true blockers, current owner, exact work location/revision, checks and evidence, remaining criteria and next action. Use existing fields and status options after reading the schema; never impose a new label system.

Ready means prerequisites proven, authority established and resources available. In progress means claimed and actually started. Accepted means the task's criteria have evidence at the current integrated revision. Map these meanings to the tracker rather than inventing status values.

An implementation can be locally checked yet await integration or device acceptance. Do not close a parent on the strength of child completion alone. For a failed or interrupted operation record the exact destination, intended delta, known saved state and uncertainty. Inspect that destination before retrying; a missing acknowledgement does not imply missing work.

Fallback when parallelism is unavailable: execute ready tasks sequentially with the same acceptance and checkpoint rules. Fallback when the tracker is inaccessible: preserve a handoff where already authorized, report unrecorded state and avoid claiming the tracker changed.

# Performance

## Mandate
Protect responsiveness and resource efficiency at representative scale without premature optimization.

## Success
Performance decisions target measured user/system-relevant bottlenecks and preserve correctness/maintainability.

## First questions
- What latency/resource constraint matters?
- Is there measurement or only suspicion?
- What data size/device/flow triggers it?
- Where is time/memory/IO actually spent?
- Can algorithm/data-flow simplification solve it before micro-optimization?

## Methods
Use representative profiling, timing/resource measurement, complexity analysis, realistic data shapes, and before/after comparison.

## Decision criteria
Prioritize proven hot paths, perceived responsiveness, asymptotic risks, and low-complexity improvements.

## Failure modes
Premature optimization; synthetic benchmarks detached from workflows; caching without invalidation semantics; performance fixes duplicating domain logic; trading correctness for unmeasured speed.

## Team interface
Product defines meaningful responsiveness; architecture/domain protect boundaries; quality establishes stable regression evidence only when useful.

## Escalate when
Measured performance blocks a primary flow or the proposed fix compromises correctness/contracts.

## Output
Measured baseline, causal evidence, selected optimization, trade-offs, and regression strategy.

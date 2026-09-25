# Expert operating model — deprecated compatibility module

The senior-collaborator behavior previously owned by this module is now normative in `KERNEL.md` and applies on every repository task that consumes the kernel.

This file remains temporarily so consumers that still select the `expert-operating-model` module can migrate without an immediate module-ID break. It adds no behavior beyond the kernel.

New or updated consumer routing must not depend on this module. Route only the materially relevant specialist roles and situation playbooks. Remove `expert-operating-model` from a consumer's selected modules when that consumer is explicitly migrated to a canonical commit containing the always-on kernel behavior.

Do not remove this compatibility module or its catalog ID until affected consumers have migrated, unless a deliberate breaking migration replaces that compatibility guarantee.

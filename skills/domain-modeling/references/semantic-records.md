# Semantic records

For a term, record its short definition, identity or value nature, meaningful relationships, and any confusing alias. Qualify the context when the same word legitimately has different meanings. Do not enforce new jargon merely for consistency.

For an invariant, record the allowed state and a concrete case that would violate it. Distinguish business truth from a source-system convention. Source field numbers and order indexes are not automatically object identities.

For a significant decision, record status, context, chosen option, reason, rejected meaningful alternative, consequences and source. A short paragraph can suffice. Link superseded records rather than erasing the history that explains current behavior.

For missing evidence, retain separate columns for observed input, proposed interpretation and open question. Do not turn an example into a universal rule without support.

Keep a domain record distinct from a caller-interface record. Domain modeling determines what an identity, state or relation means; design-interfaces determines what an external caller must supply, observe and recover from. Link them at their existing owners rather than duplicating definitions. Track changes to meaning separately from changes to its serialized shape.

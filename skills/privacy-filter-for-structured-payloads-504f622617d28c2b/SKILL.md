---
name: "privacy-filter-for-structured-payloads-504f622617d28c2b"
description: "Implements a decode-validate-freeze privacy filter for outgoing structured payloads: decodes JSON, URL, and Base64 layers before pattern matching to defeat encoding evasion, and freezes validated payloads to prevent diagnostic leaks. Use when scanning structured data before transmission to external systems or logging. Not for inbound input validation."
metadata:
  skill_id: "skl_GHbRRciJQB5Sh_p4ROpv_A"
  title: "Privacy filter for structured payloads: decode-validate-freeze to prevent encoding evasion and diagnostic leak"
  version: "skv_Wm5c9VOXUgJDaUrBFXA7Rg"
  updated: "2026-10-03T04:22:45.821477+00:00"
  canonical_url: "https://vectle.com/skills/skl_GHbRRciJQB5Sh_p4ROpv_A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[]"
---

# Privacy filter for structured payloads: decode-validate-freeze to prevent encoding evasion and diagnostic leaks

## TL;DR

Scan outgoing structured payloads for sensitive patterns using decode-validate-freeze: decode each string value through JSON, URL, and Base64 layers (max 3 rounds), validate the canonical form against your patterns, then freeze the validated payload so downstream code cannot mutate it. This defeats encoding evasion (the same path written four different ways) and prevents diagnostic leaks (never log rejected values).

## When to use

Use this when outgoing structured data must be scanned for sensitive patterns before transmission to external systems, logging infrastructure, or untrusted consumers. Applies when the serialized form can differ from semantic content through escaping, encoding, or nesting, and when validation failures must be observable without leaking the rejected values.

Common triggers: JSON payloads containing potential filesystem paths, usernames, internal URLs, or other identifying data being sent to third-party APIs, client-side logging, or analytics systems.

**When not to use this skill:** inbound user input validation (different threat model, see input-validation guidance); payloads that never leave your trust boundary; cases where full data-loss-prevention tooling already covers the egress path.

## The dual failure mode

Privacy filters commonly fail in two ways:

1. **Encoding evasion**: A regex written for plain text misses encoded forms. The path `/tmp/foo` can appear as `\/tmp\/foo` in JSON, `%2Ftmp%2Ffoo` URL-encoded, `L3RtcC9mb28=` Base64-encoded, or nested across multiple JSON-in-JSON layers. The pattern matches the wire bytes while the consumer decodes them, so the two disagree.

2. **Diagnostic leakage**: When validation rejects a payload, logging the rejected value for debugging exposes the sensitive data the filter was meant to protect. Even metadata like field paths, value hashes, or lengths can leak information or enable verification attacks.

## Procedure

### 1. Define the pattern scope explicitly

Document exactly what counts as a sensitive pattern. For filesystem paths:
- Unix absolute paths starting with forward slash
- Windows paths with drive letters or UNC format
- Relative paths with dot-slash or dot-dot-slash prefixes
- Home directory expansion forms

Explicitly list what does NOT match to avoid false positives: semantic versioning strings, URL paths in legitimate external links, code examples in documentation fields.

### 2. Multi-layer decoding in bounded rounds

Parse the structured payload. For each string value:

1. Decode JSON escapes to canonical form
2. Attempt URL decoding if the string matches percent-encoding patterns
3. Attempt Base64 decoding if the string matches Base64 alphabet and padding
4. Limit total decode rounds to 3 maximum to prevent infinite decode loops

Track each decode layer. If decoding reaches the round limit, treat the value as potentially evasive and apply the strictest validation.

### 3. Resource budgets enforced before and during validation

Apply three hard limits in order of cheapness:

- **Byte size cap**: Reject payloads exceeding a configured maximum at ingress before parsing. One megabyte is typical.
- **Parsing depth limit**: Cap nesting depth at 32 levels. Count during parsing, not via language stack depth, so overflow surfaces as a controlled denial rather than an exception.
- **Work ledger**: Charge per decoded character, per decode round, and per pattern check. Use linear-time pattern matching only: no backreferences, no lookaround, no nested quantifiers. Backtracking regex engines hide cost inside one call and cannot be metered reliably.

On any limit violation: reject immediately, emit only the limit type violated, do not process further.

### 4. Pattern matching on canonical decoded values

Apply patterns to the final decoded string, not the serialized wire bytes. Use a regex engine with guaranteed linear time complexity or explicit backtrack limits, not wall-clock timeouts which are platform-dependent and unreliable.

Prefer: RE2, Rust regex crate, or DFA-based engines. Avoid: default Python re, JavaScript RegExp, PCRE without backtrack caps.

### 5. Immutable validation to prevent TOCTOU

If validation runs asynchronously in a worker process or thread:

1. Serialize the payload to an immutable byte snapshot before validation starts
2. Validate the snapshot
3. Transmit exactly the validated bytes, never re-serialize the original object

This prevents malicious code from mutating the payload between validation and transmission.

### 6. Aggregated-only logging

On rejection, log ONLY:
- Pattern category matched from a closed enum
- Count of violations for this category in this payload
- Timestamp and correlation ID

Do NOT log:
- Field names or paths: attacker-controlled and reveal structure
- Value hashes: enable candidate verification attacks
- Value lengths: side channel that narrows search space
- Any substring or excerpt of the rejected content

For debugging false positives, rely on the correlation ID to match with sender-side logs where the full context is already known.

### 7. Bounded warning cardinality

Cap unique warning detail per time window. For example:
- Maximum 50 distinct category emissions per hour
- After cap: increment a suppression counter but emit no new log lines
- Categories are a closed enum, not derived from payload content

This prevents diagnostic explosion from becoming its own denial-of-service vector or leak channel.

### 8. Fail-closed with primary task continuation

Run the validation filter in a worker with a wall-clock deadline and memory cap. The outbound sender requires an explicit allow-transmit handle that only a successful validation produces.

On worker crash, timeout, or limit violation:
- No transmit handle is produced
- Nothing can be sent
- The supervisor returns control to the caller immediately
- Primary request processing continues with a safe denial outcome

Mark denied payloads to prevent retry loops from burning CPU. Implement a circuit breaker: after N consecutive crashes or timeouts, disable the validation worker for a cooldown period and fail all requests closed during that window.

## What this prevents

**Encoding evasion**: Multi-layer canonical decoding catches encoded forms that evade surface-level patterns.

**Resource exhaustion**: Hard budgets on size, depth, and work prevent malicious payloads from causing denial of service through the validator itself.

**Diagnostic leakage**: Aggregated-only logging ensures rejection events are observable without exposing the sensitive content that triggered the filter, and without creating side channels through metadata.

**Race conditions**: Immutable snapshot validation prevents mutation between check and transmission.

**Operational collapse**: Fail-closed worker isolation with circuit breaking ensures validation complexity or instability cannot block the primary request path.

## Limitations and known gaps

This procedure is based on reasoned analysis of common encoding evasion and diagnostic leak patterns, not on executed tests or production deployment data.

**What it does not cover**:

- Sensitive data in non-string types: integers, booleans, or structured keys
- Information leaked through field presence or absence rather than values
- Timing side channels where validation duration varies with content
- Allowlist mechanisms for legitimate mentions of paths in documentation
- Pattern maintenance as new encoding schemes emerge
- Cross-boundary consistency when different systems use different parsers

**Deployment prerequisites**:

- A regex engine with linear-time guarantees or explicit backtrack limits
- Immutable data structures or copy-on-validate discipline in the validation worker
- Monitoring for circuit breaker activation and suppression counter growth
- Clear documentation of what patterns match so callers know what will be blocked

**When not to use**:

- For allowlist validation where the permitted set is small and enumerable: exact matching is simpler
- When the consumer and validator use different parsers with different lenience: results will disagree
- For real-time high-throughput paths where validation latency is unacceptable: consider sampling or async post-transmission auditing instead

## Relation to existing guidance

This builds on established patterns for resource budgeting, fail-closed validation, and encoding normalization, but combines them specifically for privacy-sensitive structured data where diagnostic transparency usually conflicts with data protection. The multi-layer decode procedure and aggregated-only logging discipline are the novel elements addressing gaps found in simpler approaches.

## Compatibility

- Language-agnostic procedure; implementable in Python, TypeScript, Go, or Rust.
- Linear-time pattern matching only: no backreferences, no lookaround, no nested quantifiers.

## Variant phrasings

- privacy filter structured payloads encoding evasion
- prevent sensitive data leak JSON logging
- decode validate freeze pattern
- diagnostic leak validation rejected values


---

Source: [Vectle](https://vectle.com/skills/skl_GHbRRciJQB5Sh_p4ROpv_A). Version: `skv_Wm5c9VOXUgJDaUrBFXA7Rg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

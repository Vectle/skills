---
name: "fix-confluent-kafka-build-error-librdk-075b12277bb50763"
description: "Fixes installing confluent-kafka from source failing with 'librdkafka/rdkafka.h file not found'. Use this when pip tries to compile and the C headers are missing. Not for other build errors."
metadata:
  skill_id: "skl_3sPI8369qmhUDw6xPx8xuA"
  title: "Fix confluent-kafka build error: librdkafka/rdkafka.h file not found"
  version: "skv_f8Ej87ufIgacpbRIaI59dw"
  updated: "2026-10-03T05:09:41.127534+00:00"
  canonical_url: "https://vectle.com/skills/skl_3sPI8369qmhUDw6xPx8xuA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_0n8FFrTDtnM1W_130JQ93g\",\"https://github.com/confluentinc/confluent-kafka-python/issues/184\"]"
---

TL;DR: if installing confluent-kafka from source fails with `fatal error: 'librdkafka/rdkafka.h' file not found`, the build needs the librdkafka C library headers first. Fastest fix on a modern release: `pip install -U confluent-kafka` to a version with bundled binary wheels (0.11.4+), which never compiles anything. If you must build from source, install librdkafka first (`brew install librdkafka` on macOS, your system package elsewhere) so the headers are on the include path.

```text
fatal error: 'librdkafka/rdkafka.h' file not found
```

## Steps

1. Try the wheels first:

```sh
pip install -U confluent-kafka
```

   Expected: a binary wheel installs, no compilation. Success check: `import confluent_kafka` works.

2. If you must compile, install librdkafka via your system package manager first.

## When to use this

- Source build fails on the missing rdkafka.h.

## When NOT to use this

- Other compile errors; read the message.
- Wheels already install fine; nothing to do.

## Compatibility

- confluent-kafka 0.11.4+ (bundled wheels).

## Variant phrasings

- "confluent-kafka rdkafka.h not found"
- "confluent kafka build error librdkafka"

## Root cause

The Python package wraps a C library; without its headers the C extension cannot build.

## Edge cases

- The maintainers added bundled wheels precisely because this kept biting people; prefer them.

Source: https://github.com/confluentinc/confluent-kafka-python/issues/184

---

Source: [Vectle](https://vectle.com/skills/skl_3sPI8369qmhUDw6xPx8xuA). Version: `skv_f8Ej87ufIgacpbRIaI59dw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

---
name: "redpanda-cloud-requires-tls-before-sas-14355e1a57849721"
description: "When connecting to Redpanda Cloud, always enable TLS before SASL; a bare SASL attempt fails the handshake."
metadata:
  skill_id: "skl_MPO1di4oojTf0KAm-PWhHg"
  title: "Redpanda Cloud requires TLS before SASL; enable TLS first, then SCRAM-SHA-256"
  version: "skv_Ap9eDtjq55CL57fFZiYIXw"
  updated: "2026-10-03T04:38:04.713855+00:00"
  canonical_url: "https://vectle.com/skills/skl_MPO1di4oojTf0KAm-PWhHg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Redpanda Cloud requires TLS before SASL; enable TLS first, then SCRAM-SHA-256

## TL;DR

When connecting to Redpanda Cloud, always enable TLS before SASL; a bare SASL attempt fails the handshake. Use SCRAM-SHA-256 (or SCRAM-SHA-512) with your Cloud-generated username and password, and point at seed-[id].cloud.redpanda.com:9092. If you see unknown SASL mechanism, switch to one the broker supports.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

Tool: Redpanda. The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

If you see TOPIC_AUTHORIZATION_FAILED, the credentials work but the user lacks an ACL; grant it with rpk security acl create instead of regenerating credentials.

Context: Official docs (redpanda-data/skills, connect-debugging failure modes): documents the connection-order gotcha that trips agents wiring Kafka clients to Redpanda Cloud. A 'SASL auth failure: SASL handshake first' error means the broker requires TLS before SASL, so the client must enable TLS first and then SASL. The supported Cloud connect pattern is TLS enabled plus SCRAM-SHA-256 against the seed hostname on port 9092.


---

Source: [Vectle](https://vectle.com/skills/skl_MPO1di4oojTf0KAm-PWhHg). Version: `skv_Ap9eDtjq55CL57fFZiYIXw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

---
name: "is-the-or-operator-supported-in-scylla-70f9cb443e8188b6"
description: "Shows how to fix is the OR operator supported in ScyllaDB?. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_NQZ5fIBhEFXuXiO4V5iboQ"
  title: "Is the OR operator supported in ScyllaDB?"
  version: "skv_sRMojbRjd69DyvGlkUejQQ"
  updated: "2026-10-04T06:33:00.321083+00:00"
  canonical_url: "https://vectle.com/skills/skl_NQZ5fIBhEFXuXiO4V5iboQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/75832433/is-the-or-operator-supported-in-scylladb\"]"
---

## TL;DR

In your use case, where email='[recipient email]' or email='robs@ex', the solution is simple - just use the IN keyword: where email IN ('[recipient email]', 'robs@ex').

## Steps

1. CQL (the Cassandra Query Language, also implemented by ScyllaDB), does not have a general-purpose "OR" keyword (see issue #12910 - only "AND" is supported). The error message could have been, and should have been, friendlier (see issue #1703), but ultimately tells you the right thing - that it's a syntax error - OR is not legal CQL syntax. In your use case, `where email='[recipient email]' or email='robs@ex'`, the solution is simple - just use the IN keyword: `where email IN ('[recipient email]', 'robs@ex')`. By the way, the `1=1` part also doesn't work, not even without OR, because currently CQL expressions are rather limited in their scope, in this case `column=value` is a valid expression, but `value=value` or other stuff, is not. Issue #12906 is one step towards improving that, but for your use case you don't really need it (you didn't really want to use `1=1` in your expression).

``` cqlsh> select * from test.d_emp where email='[recipient email]'; id | dept | email | first_name | last_name | salary -----+------+-------------+------------+-----------+-------- 10 | 10 | [recipient email] | Rob | Stark | 1000 1 | 10 | [recipient email] | Rob | Stark | 1000 101 | 10 | [recipient email] | Rob | Stark | 1000 (3 rows) ```

2. However if I use two conditions using OR operator it is giving syntax error. Even a simple 1=1...

## When to use

You are seeing this: CQL (the Cassandra Query Language, also implemented by ScyllaDB), does not have a general-purpose "OR" keyword (see issue #12910 - only "AND" is supported). Use this skill when you run into "Is the OR operator supported in ScyllaDB?".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_NQZ5fIBhEFXuXiO4V5iboQ). Version: `skv_sRMojbRjd69DyvGlkUejQQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

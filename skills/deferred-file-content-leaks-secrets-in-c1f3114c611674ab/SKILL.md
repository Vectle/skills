---
name: "deferred-file-content-leaks-secrets-in-c1f3114c611674ab"
description: "Fixes deferred file content leaking secrets into Puppet agent output by setting preprocess_deferred = true in puppet.conf. Use when a stdlib::deferrable_epp file resource renders secrets in plain text on change with agent 8.x. Not for leaks from non-deferred resources."
metadata:
  skill_id: "skl_S5mpOa1de0sivWWspTpKBw"
  title: "Deferred file content leaks secrets into puppet agent output"
  version: "skv_WWxxJ1DBQqla-OybKrYRHA"
  updated: "2026-10-03T04:23:57.800998+00:00"
  canonical_url: "https://vectle.com/skills/skl_S5mpOa1de0sivWWspTpKBw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Set `preprocess_deferred = true` in puppet.conf. In agent 8 the default flipped to false, so deferred values get rendered into the diff in plain text; turning preprocessing back on restores the 7.x behavior where Sensitive values stay redacted.

## The problem

A file resource using `stdlib::deferrable_epp` renders the new secret in plain text in the agent output whenever it changes.

## Fix it

1. Confirm the leak is from a deferred value: the resource uses `stdlib::deferrable_epp` and the agent is 8.x.
   Success check: agent 8.5 shows the secret in the output diff.

2. Set in puppet.conf:
   ```ini
   [agent]
   preprocess_deferred = true
   ```
   Success check: the setting is present in the agent config.

3. Re-run the agent.
   Success check: the secret renders as redacted in the output.

## When this applies

- Puppet agent 8.x with `stdlib::deferrable_epp` file resources.
- Secrets appear in clear text in agent output when the deferred resource changes.

## When it does not apply

- A plain `Sensitive` value on a non-deferred resource leaks; that redacts fine already, so the cause is different.
- Agent 7.x; the default was already true there.

## Compatibility

- Puppet agent 8.x (default false), 7.x (default true). puppetlabs-stdlib with deferrable_epp.

## Variant phrasings

- puppet deferred secrets plain text agent output
- preprocess_deferred secret leak
- stdlib deferrable_epp sensitive redacted

## Why it happens

Agent 8 changed the default of `preprocess_deferred` to false, meaning deferred values are rendered into the change diff before the Sensitive redaction pass can hide them. Re-enabling preprocessing restores the 7.x ordering.

## Edge cases

- Audit other deferred resources after the change; any deferred value benefits from the same setting.


---

Source: [Vectle](https://vectle.com/skills/skl_S5mpOa1de0sivWWspTpKBw). Version: `skv_WWxxJ1DBQqla-OybKrYRHA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

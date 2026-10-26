---
name: "missing-python-3-10-wheels-for-oso-0-2-c7ff36b89cf81add"
description: "Shows how to fix missing Python 3.10 wheels for oso 0.22.1 (pip install fails). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_TU6tPwEK94GN_zzDPfuEfw"
  title: "Missing Python 3.10 wheels for oso 0.22.1 (pip install fails)"
  version: "skv_x8y01nxy4PrPIAOpctpg0Q"
  updated: "2026-10-03T14:00:46.081539+00:00"
  canonical_url: "https://vectle.com/skills/skl_TU6tPwEK94GN_zzDPfuEfw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_yl2Bx72Jc1w6BpnWWomjVw\",\"https://github.com/osohq/oso/issues/1354\"]"
---

## TL;DR

Oso 0.22.1 on PyPI had no wheels for Python 3.10 and no source distribution either, so pip install oso failed on the latest stable Python. cibuildwheel supported 3.10, but the release artifacts had not been built for it.

## Steps

1. Oso 0.22.1 on PyPI had no wheels for Python 3.10 and no source distribution either, so pip install oso failed on the latest stable Python. cibuildwheel supported 3.10, but the release artifacts had not been built for it. The reporter pointed at cibuildwheel 2.1.3 as the tooling that could produce the missing wheels.

2. The maintainer built and uploaded the Python 3.10 wheels to PyPI for oso 0.22.1, so a plain pip install works again. If you hit this on an old pinned version, upgrade to the re-released 0.22.1 (or newer); the reporter confirmed it installs fine after the wheels were published. The maintainer also attached the wheel archive to the issue for anyone who could not wait for the PyPI upload.

## When to use

You are seeing this: The reporter pointed at cibuildwheel 2.1.3 as the tooling that could produce the missing wheels. Use this skill when you run into "Missing Python 3.10 wheels for oso 0.22.1 (pip install fails)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: Oso 0.22.1, cibuildwheel 2.1.3. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_TU6tPwEK94GN_zzDPfuEfw). Version: `skv_x8y01nxy4PrPIAOpctpg0Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

---
name: "deprecated-flowcontrol-api-warning-sti-1886f5797ffbd6f2"
description: "Shows how to fix deprecated flowcontrol API warning still appears on newer Lacework agent versions. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_JLhJ6Uyp8x0dPTBBPwKogQ"
  title: "Deprecated flowcontrol API warning still appears on newer Lacework agent versions"
  version: "skv_GB_dNsCCgpy8iCtildy5pg"
  updated: "2026-10-03T14:10:01.98454+00:00"
  canonical_url: "https://vectle.com/skills/skl_JLhJ6Uyp8x0dPTBBPwKogQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The agent samples the API where it exists and ignores it where it does not, so the deprecation warning on 1.29+ is a false positive from API discovery. The warning is wrong on newer clusters.

## Steps

1. The warning is wrong on newer clusters. The agent samples the API where it exists and ignores it where it does not, so the deprecation warning on 1.29+ is a false positive from API discovery. The reporter accepted this explanation.

## When to use

You are seeing this: On recent agent versions the Kubernetes API deprecation dashboard still flags /apis/flowcontrol.apiserver.k8s.io/v1beta2/flowschemas usage. Use this skill when you run into "Deprecated flowcontrol API warning still appears on newer Lacework agent versions".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_JLhJ6Uyp8x0dPTBBPwKogQ). Version: `skv_GB_dNsCCgpy8iCtildy5pg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

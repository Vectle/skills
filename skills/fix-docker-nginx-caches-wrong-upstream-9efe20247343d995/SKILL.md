---
name: "fix-docker-nginx-caches-wrong-upstream-9efe20247343d995"
description: "Dify: fix(docker): nginx caches wrong upstream IP after restart when host DNS search domains resolve service names externally. The verified fix is Fix: Contributor kanson1996 diagnosed: nginx resolved upstream service names to IPs once at startup and cached them, so after a container restart the IP was stale whenever host DNS search domains resolved the service names externally. Use this when you hit the symptoms above in dify; not for unrelated dify errors or general setup questions."
metadata:
  skill_id: "skl_aq7G2QLRiNXE_vcRknXYMw"
  title: "fix(docker): nginx caches wrong upstream IP after restart when host DNS search domains resolve service names externally"
  version: "skv__vNxONydB-jR-ox4irb-IA"
  updated: "2026-10-03T05:55:39.763132+00:00"
  canonical_url: "https://vectle.com/skills/skl_aq7G2QLRiNXE_vcRknXYMw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Contributor kanson1996 diagnosed: nginx resolved upstream service names to IPs once at startup and cached them, so after a container restart the IP was stale whenever host DNS search domains resolved the service names externally. Fixed by merged PR #39155 ('use dynamic DNS resolution for all nginx upstreams') on 2026-08-11 - upgrade to a build containing that fix.

## The error

```text
Issue langgenius/dify#39154 (closed, 60 comments): ### Self Checks - [x] I have read the [Contributing Guide](https://github.com/langgenius/dify/blob/main/CONTRIBUTING.md) and [Language Policy](https://github.com/langgenius/dify/issues/1542). - [x] This is only for bug report, if you would like to ask a question, please head to [Discussions](https://github.com/langgenius/dify/discussions/categories/general). - [x] I have searched for existing issues [search for existing issues](https://github.com/langgenius/dify/issues), including closed ones. - [x] I confirm that I am using English to submit this report, otherwise it will be closed. - [x] 【中文
```

## Fix

1. Contributor kanson1996 diagnosed: nginx resolved upstream service names to IPs once at startup and cached them, so after a container restart the IP was stale whenever host DNS search domains resolved the service names externally.
2. Fixed by merged PR #39155 ('use dynamic DNS resolution for all nginx upstreams') on 2026-08-11 - upgrade to a build containing that fix.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in dify.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in dify, even a similar-looking one.
- General dify setup or credential questions.

## Compatibility

- Dify (langgenius/dify)

## Variant phrasings

- How to fix "fix(docker): nginx caches wrong upstream IP after restart when host DNS search domains resolve service names externally" in dify
- dify: fix(docker): nginx caches wrong upstream IP after restart when host DNS search domains resolve service names externally

## Source

- https://github.com/langgenius/dify/issues/39154

---

Source: [Vectle](https://vectle.com/skills/skl_aq7G2QLRiNXE_vcRknXYMw). Version: `skv__vNxONydB-jR-ox4irb-IA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

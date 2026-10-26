---
name: "react-fc-returns-reactnode-since-18-2-e0d5527b0d3067e2"
description: "Shows how to fix react.FC returns ReactNode since 18.2. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_hmsAEqRz_eRjyfQA7vvC5g"
  title: "React.FC returns ReactNode since 18.2"
  version: "skv_t-O3V41BvMSt2KEVgkPy1A"
  updated: "2026-10-04T06:10:23.040385+00:00"
  canonical_url: "https://vectle.com/skills/skl_hmsAEqRz_eRjyfQA7vvC5g"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/resend/resend-node/issues/124\"]"
---

## TL;DR

Issue resend/resend-node#124 (closed, 5 comments): Upgraded to the latest version of @types/react and a FunctionalComponent no longer returns a ReactElement which resend expects, instead a ReactNode is returned From the @types/react codebase:

## Steps

1. Issue resend/resend-node#124 (closed, 5 comments): Upgraded to the latest version of `@types/react` and a `FunctionalComponent` no longer returns a `ReactElement` which resend expects, instead a `ReactNode` is returned

2. From the `@types/react` codebase:

3. [jayanratna / vcapretz (maintainers)]: Updating the SDK's React.FC types alone wasn't enough - the underlying @react-email render function needed the matching change too. Typing improvements shipped via PR #401; maintainers asked anyone still seeing this on the latest Resend SDK + React versions to reopen. Community workaround: drop the React.FC annotation and declare the email as a plain JSX function.

## When to use

You are seeing this: ``ts interface FunctionComponent[P = {}] { (props: P, context?: any): ReactElement[any, any] | null; propTypes?: WeakValidationMap[P] | undefined; contextTypes?: ValidationMap[any] | undefined; defaultProps?: Partial[P] | undefined; displayName?: string |... Use this skill when you run into "React.FC returns ReactNode since 18.2".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 18.0.28, 18.2.14. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_hmsAEqRz_eRjyfQA7vvC5g). Version: `skv_t-O3V41BvMSt2KEVgkPy1A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

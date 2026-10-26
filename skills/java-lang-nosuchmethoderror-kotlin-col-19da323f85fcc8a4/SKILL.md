---
name: "java-lang-nosuchmethoderror-kotlin-col-19da323f85fcc8a4"
description: "Fixes java.lang.NoSuchMethodError: kotlin.collections.ArraysKt.copyInto when initializing the Harness Java SDK CfClient in Spring Boot, by upgrading Spring Boot to 2.7.x or forcing a newer kotlin-stdlib. Use when the SDK init throws this error from okio. Not for other NoSuchMethodErrors."
metadata:
  skill_id: "skl_ENNUgGMSw_maor79CNSySw"
  title: "java.lang.NoSuchMethodError: kotlin.collections.ArraysKt.copyInto with the Harness Java SDK in Spring Boot"
  version: "skv_wTIHOrsMGaWraCaaxkrVaQ"
  updated: "2026-10-03T04:10:27.300878+00:00"
  canonical_url: "https://vectle.com/skills/skl_ENNUgGMSw_maor79CNSySw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_m78ErwSXnBo2qq3hufoK7w\",\"https://github.com/harness/ff-java-server-sdk/issues/131\"]"
---

## TL;DR

Upgrade Spring Boot to 2.7.x, which brings a compatible kotlin-stdlib. If you cannot upgrade, add a newer kotlin-stdlib directly to your dependencies to force the version. This is a classpath conflict, not a bug in the Harness SDK.

## The error

```text
java.lang.NoSuchMethodError: kotlin.collections.ArraysKt.copyInto
```

Thrown when initializing the Harness Java SDK `CfClient` in a Spring Boot project; the stack points through okio.

## Fix it

1. Check the resolved kotlin-stdlib version:
   ```bash
   ./mvnw dependency:tree -Dincludes=org.jetbrains.kotlin:kotlin-stdlib
   ```
   Success check: the tree shows kotlin-stdlib 1.2.x (the conflicting version).

2. Preferred: upgrade Spring Boot to 2.7.x.
   Success check: the dependency tree now resolves kotlin-stdlib to a 1.6+ version.

3. If you cannot upgrade Spring Boot, force the stdlib version directly in your build file:
   ```xml
   [dependency]
     [groupId]org.jetbrains.kotlin[/groupId]
     [artifactId]kotlin-stdlib[/artifactId]
     [version]1.6.21[/version]
   [/dependency]
   ```
   Success check: the dependency tree shows the forced version winning.

4. Rebuild and initialize the CfClient.
   Success check: no NoSuchMethodError at startup.

## When this applies

- Harness Java SDK CfClient init throws `NoSuchMethodError: kotlin.collections.ArraysKt.copyInto`.
- Spring Boot project pulling kotlin-stdlib 1.2.x alongside okhttp 4.9.x.

## When it does not apply

- A different `NoSuchMethodError` (different class or method); that is a different version conflict.
- You do not use the Harness SDK or okio at all.
- The error occurs at compile time rather than runtime.

## Compatibility

- Spring Boot 2.7.x brings a compatible kotlin-stdlib. Older Spring Boot (2.3–2.6) may pull 1.2.x.
- okhttp 4.9.x requires kotlin-stdlib 1.4+.

## Variant phrasings

- Harness Java SDK NoSuchMethodError ArraysKt.copyInto
- kotlin.collections.ArraysKt.copyInto Spring Boot
- CfClient init NoSuchMethodError okio

## Why it happens

Older Spring Boot versions pull in kotlin-stdlib 1.2.x, which lacks `ArraysKt.copyInto`. okhttp 4.9.x (used by the Harness SDK) needs that method, so the JVM links against the old stdlib at runtime and throws NoSuchMethodError. Upgrading Spring Boot or forcing the stdlib aligns the versions.

## Edge cases

- Gradle: use a strict version constraint or `force` on kotlin-stdlib instead of the Maven snippet.
- If another library pins kotlin-stdlib below 1.4, you may need dependency exclusions as well.


---

Source: [Vectle](https://vectle.com/skills/skl_ENNUgGMSw_maor79CNSySw). Version: `skv_wTIHOrsMGaWraCaaxkrVaQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

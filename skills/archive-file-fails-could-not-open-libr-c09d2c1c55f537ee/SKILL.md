---
name: "archive-file-fails-could-not-open-libr-c09d2c1c55f537ee"
description: "Fixes Chef archive_file failing on CentOS/RHEL 7 with 'Could not open library libarchive.so.13, XZ_5.2 not found'. Use this on Infra Client 17.7 on CentOS/RHEL 7. Not for CentOS/RHEL 8 or for other LoadErrors."
metadata:
  skill_id: "skl_-DHmjeQYIm0ew6iJeu_Rig"
  title: "archive_file fails: Could not open library libarchive.so.13, XZ_5.2 not found (CentOS 7)"
  version: "skv_taspdpGTTXepJ2AaF76rBA"
  updated: "2026-10-03T05:05:21.21022+00:00"
  canonical_url: "https://vectle.com/skills/skl_-DHmjeQYIm0ew6iJeu_Rig"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if the `archive_file` resource fails on Infra Client 17.7 with `LoadError: Could not open library 'libarchive.so.13': /lib64/liblzma.so.5: version 'XZ_5.2' not found` on CentOS 7 / RHEL 7, the OS is at fault: libnss_myhostname drags in libdw and liblzma, whose versions clash with the omnibus libarchive (which should never load system libraries outside /opt). Edit /etc/nsswitch.conf and change the hosts line from `hosts: files dns myhostname` to `hosts: files dns`. This stops the myhostname NSS module (and its libdw chain) from loading, and archive_file works again. The issue does not occur on CentOS/RHEL 8.

```text
LoadError: Could not open library 'libarchive.so.13': /lib64/liblzma.so.5: version `XZ_5.2' not found
```

## Steps

1. Edit /etc/nsswitch.conf: change `hosts: files dns myhostname` to `hosts: files dns`.

2. Re-run the Chef recipe.

   Expected: archive_file works. Success check: no more LoadError.

## When to use this

- CentOS/RHEL 7, Infra Client 17.7, the exact XZ_5.2 LoadError.

## When NOT to use this

- CentOS/RHEL 8; the dependency chain does not exist there.
- Other LoadErrors; read the actual missing symbol.

## Compatibility

- Chef Infra Client 17.7 on CentOS/RHEL 7.

## Variant phrasings

- "chef archive_file libarchive XZ_5.2"
- "chef Could not open library libarchive.so.13"

## Root cause

The myhostname NSS module pulled libdw, which pulled a liblzma incompatible with the omnibus libarchive's expectations.

## Edge cases

- Removing myhostname from nsswitch can affect hostname resolution edge cases; test name lookups after the change.

Source: https://github.com/chef/chef/issues/12228

---

Source: [Vectle](https://vectle.com/skills/skl_-DHmjeQYIm0ew6iJeu_Rig). Version: `skv_taspdpGTTXepJ2AaF76rBA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

---
name: "error-loading-shared-library-libresolv-d453085f56ce2bd6"
description: "Shows how to fix error loading shared library libresolv.so.2 : No such file or directory (needed by /lib/libclntsh.so). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_uT5bBJKaTu3UM29nGkMbow"
  title: "Error loading shared library libresolv.so.2 : No such file or directory (needed by /lib/libclntsh.so)"
  version: "skv_q_R4E04WC-2dFcpC9J6qFQ"
  updated: "2026-10-04T07:18:19.201254+00:00"
  canonical_url: "https://vectle.com/skills/skl_uT5bBJKaTu3UM29nGkMbow"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "Error loading shared library libnsl.so.1: N o such file or directory (needed by /lib/libclntsh.so)": i fixed the problem `` RUN chmod 755 /usr/local/bin/docker-entrypoint.sh && \ mkdir /opt/oracle && \ cd /opt/oracle && \ curl -OL download.oracle.com/otn\_software/linux/instantclient/19600/instantclient-basic-linux.x64-19.6.0.0.0dbru.zip && \ unzip instantclient-basic-linux.x64-19.6.0.0.0dbru.zip && \ rm -rf instantclient-basic-linux.x64-19.6.0.0.0dbru.zip && \ cd /opt/oracle/instantclient\_19\_6 && \ ln -s /usr/lib/libnsl.so.2 /usr/lib/libnsl.so.1 && \ ln -s /lib/libc.so.6 /usr/lib/libre

```text
Error loading shared library libnsl.so.1: N o such file or directory (needed by /lib/libclntsh.so)
```

## Steps

1. ``` RUN chmod 755 /usr/local/bin/docker-entrypoint.sh && \ mkdir /opt/oracle && \ cd /opt/oracle && \ curl -OL download.oracle.com/otn_software/linux/instantclient/19600/instantclient-basic-linux.x64-19.6.0.0.0dbru.zip && \ unzip instantclient-basic-linux.x64-19.6.0.0.0dbru.zip && \ rm -rf instantclient-basic-linux.x64-19.6.0.0.0dbru.zip && \ cd /opt/oracle/instantclient_19_6 && \ ln -s /usr/lib/libnsl.so.2 /usr/lib/libnsl.so.1 && \ ln -s /lib/libc.so.6 /usr/lib/libresolv.so.2 && \ apk add --no-cache libaio libnsl libc6-compat && \ echo "export LD_LIBRARY_PATH=/opt/oracle/mount the host path instantclient_19_6 at container path /lib64:$LD_LIBRARY_PATH" >> /etc/profile.d/oracle_client.sh && \ echo "export PATH=/opt/oracle/instantclient_19_6:$PATH" >> /etc/profile.d/oracle_client.sh ```

2. Also searched as: "loading shared library libresolv.so.2 : No such file or directory (needed by /lib/libclntsh.so)"

## When to use

You are seeing this: Also searched as: "loading shared library libresolv.so.2 : No such file or directory (needed by /lib/libclntsh.so)" Use this skill when you run into "Error loading shared library libresolv.so.2 : No such file or directory (needed by /lib/libclntsh.so)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 19.6.0.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Edge cases

- Also searched as: "loading shared library libresolv.so.2 : No such file or directory (needed by /lib/libclntsh.so)"


---

Source: [Vectle](https://vectle.com/skills/skl_uT5bBJKaTu3UM29nGkMbow). Version: `skv_q_R4E04WC-2dFcpC9J6qFQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

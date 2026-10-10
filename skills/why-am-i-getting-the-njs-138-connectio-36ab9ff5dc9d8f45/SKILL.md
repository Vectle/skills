---
name: "why-am-i-getting-the-njs-138-connectio-36ab9ff5dc9d8f45"
description: "Shows how to fix why am I getting the \"NJS-138: connections to this database server version are not supported by node-oracledb in. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_6-0Z4K_GRmkpn3H_jcAtOQ"
  title: "Why am I getting the \"NJS-138: connections to this database server version are not supported by node-oracledb in"
  version: "skv_QhdZWj8oubZc-BaTkC24LQ"
  updated: "2026-10-04T08:27:00.865167+00:00"
  canonical_url: "https://vectle.com/skills/skl_6-0Z4K_GRmkpn3H_jcAtOQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

I ran the following simple app using node-oracledb 6.0.1 in Thin mode: ``` const oracledb = require('oracledb'); async function runApp() { let connection; let dbConfig = { user : "scott", password - "tiger", connectString : "YOUR_HOST/orclpdb" }; //oracledb.initOracleClient(); // Get a standalone Oracle Database connection connection = await oracledb.getConnection(dbConfig); console.log('Connection was successful!'); // Run a simple SQL on the...

## Steps

1. node-oracledb 6.0 Thin mode supports Oracle Database Release 12.1 and later. Please see the following documentation: node-oracledb.readthedocs.io/en/latest/user_guide/appendix_a.html#id1 for the supported Oracle releases for both the Thin and Thick modes. Node-oracledb 6.0 is a 'Thin mode' driver by default. You can switch to Thick mode for Oracle Database 11g support or upgrade your database version.

## When to use

You are seeing this: node-oracledb 6.0 Thin mode supports Oracle Database Release 12.1 and later. Use this skill when you run into "Why am I getting the "NJS-138: connections to this database server version are not supported by node-oracledb in".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 12.1, node-oracledb 6.0.1. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_6-0Z4K_GRmkpn3H_jcAtOQ). Version: `skv_QhdZWj8oubZc-BaTkC24LQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

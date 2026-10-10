---
name: "postgres-mcp-mcp-error-32603-self-sign-987377abec102b57"
description: "Fixes the Postgres MCP server failing against AWS RDS with a self-signed certificate error. Use when tool calls fail with MCP error -32603: self-signed certificate in certificate chain against RDS or another SSL-mandatory host. Not for wrong passwords or unreachable hosts."
metadata:
  skill_id: "skl_IhU7J24N95lIyFVa5NuWhg"
  title: "Postgres MCP: MCP error -32603 self-signed certificate in certificate chain (RDS)"
  version: "skv_t8P1PUYqoF-r_B92PzOQcA"
  updated: "2026-10-03T04:34:05.261333+00:00"
  canonical_url: "https://vectle.com/skills/skl_IhU7J24N95lIyFVa5NuWhg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix Postgres MCP `MCP error -32603: self-signed certificate in certificate chain`

## TL;DR
Add `?sslmode=require&rejectUnauthorized=false` to your connection string when connecting to AWS RDS. RDS presents certificates your local trust store does not recognize, and the server's postgres driver fails the handshake on validation.

The exact error:

```text
MCP error -32603: self-signed certificate in certificate chain
```

## Steps

### 1. Confirm SSL is the problem
Check that a plain psql connection works with SSL required:

```bash
psql "postgresql://[user]@[rds host]:5432/[db]?sslmode=require"
```

Success check: psql connects. If it fails too, fix the database connectivity first; this is not an MCP problem.

### 2. Update the connection string in the MCP config
In your MCP config, set the postgres entry's connection string to:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://[rds host]:5432/[db]?sslmode=require&rejectUnauthorized=false"
      }
    }
  }
}
```

Success check: the string contains both `sslmode=require` and `rejectUnauthorized=false`.
Put your database username and password in the URL ahead of the host in the usual `user:password@host` form.

### 3. Restart and run a read-only query
Restart the client and ask it to list tables or run a simple select.

Success check: results come back instead of the -32603 error.

## When this applies
- You connect the Postgres MCP server to AWS RDS (or any host with a self-signed / private-CA certificate) and every call fails with `self-signed certificate in certificate chain`.

## When it does not apply
- `password authentication failed` or `could not connect to server`. Those are credential or network problems: check the password (URL-encode special characters), the security group, and that the host is reachable.
- Local Postgres without SSL. Do not add the SSL parameters; a plain connection string with your local user and password is correct there.

## Tool compatibility
- @modelcontextprotocol/server-postgres (reference server; note it is now archived, community forks like crystaldba/postgres-mcp are the maintained path)
- AWS RDS PostgreSQL and other SSL-mandatory hosts
- Node.js 18+

## Why it happens
RDS terminates TLS with certificates issued by Amazon's CA, which is often absent from the default trust store the server's postgres driver uses. The driver validates the chain, finds a certificate it cannot verify, and aborts with the self-signed-chain error. The `rejectUnauthorized=false` parameter tells the driver to accept the chain anyway, matching what `psql` does when you accept the cert interactively.

## Edge cases
- `rejectUnauthorized=false` disables validation; on untrusted networks prefer `rejectUnauthorized=true` with Amazon's CA bundle installed locally.
- If your password contains `@`, `/`, `?`, or `#`, percent-encode it or the URL parser will misread the connection string and you will get auth failures instead.
- The reference server was archived in 2025; if you hit new issues, the crystaldba/postgres-mcp community fork is the maintained successor.

---

Source: [Vectle](https://vectle.com/skills/skl_IhU7J24N95lIyFVa5NuWhg). Version: `skv_t8P1PUYqoF-r_B92PzOQcA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

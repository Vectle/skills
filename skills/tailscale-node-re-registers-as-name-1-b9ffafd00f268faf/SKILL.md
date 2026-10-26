---
name: "tailscale-node-re-registers-as-name-1-b9ffafd00f268faf"
description: "Fixes a tailscale node coming back as NAME-1 in the admin console after docker compose down -v. Use when the node name gains a numeric suffix after recreating containers. Covers keeping the state volume so the node keeps its identity. Not for auth key problems."
metadata:
  skill_id: "skl_GaP2jhw4FvniJjAFSBFwiQ"
  title: "tailscale node re-registers as NAME-1 after docker compose down -v"
  version: "skv_ehhuHXN-a6yPCZqfJzeTzg"
  updated: "2026-10-03T06:00:26.16826+00:00"
  canonical_url: "https://vectle.com/skills/skl_GaP2jhw4FvniJjAFSBFwiQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/ciram-co/selfhost-buzz/blob/HEAD/docs/tailscale.md\"]"
---

# tailscale node re-registers as NAME-1 after docker compose down -v

TL;DR: `docker compose down -v` deleted the volume holding tailscale's state, so the node forgot its identity and registered as a brand-new machine with a -1 suffix. Keep the state volume (drop the `-v`, or declare the volume external) and the name stays put.

```text
symptom: your node was "homelab", and after recreating the containers
"homelab-1" appears in the admin console as a separate machine
```

## Steps

1. Stop deleting the state volume. Recreate without `-v`:

```bash
docker compose down
docker compose up -d
```

Expected: the node rejoins with its original name.

2. For a durable fix, declare the tailscale state volume as external in compose so no command wipes it:

```yaml
volumes:
  tailscale-state:
    external: true
```

Expected: future `down -v` runs leave the state volume alone.

3. Remove the stray -1 duplicate from the admin console machines list.

Expected: one entry per real node again.

## When this applies

- node names gain -1, -2 suffixes after container recreation
- ACLs or DNS entries target the old name and break after the rename
- any Docker setup storing tailscale state in a compose-managed volume

## When it doesnt

- `authkey already used` errors — that is key reuse, not state loss
- the name changes on a bare-metal install — no volumes involved there
- two genuinely different machines — they are supposed to have different names

## Compatibility

tailscale in Docker Compose with state in a named volume.

## Other phrasings

- `tailscale docker duplicate machine after down -v`
- `tailscale node name changed to -1`

## Why it happens

Tailscale's node identity lives in its state directory. Delete the directory and the next start looks like a new machine; the control plane keeps the old name taken, so the newcomer gets a numeric suffix. The `-v` flag is what wipes the anonymous and named volumes.

## Edge cases

- If the state is already gone, you cannot recover the old identity; accept the new name or re-key the node deliberately.
- External volumes must be created once by hand before first `up`, or compose will complain.


---

Source: [Vectle](https://vectle.com/skills/skl_GaP2jhw4FvniJjAFSBFwiQ). Version: `skv_ehhuHXN-a6yPCZqfJzeTzg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

---
name: "data-exfiltration-signals-to-watch-for-ba26df05b1605580"
description: "A guide to data-exfiltration signals: outbound volume anomalies, DNS tunneling patterns, personal cloud uploads, off-hours transfers, and how to confirm before accusing. Use when investigating suspected data theft or building exfiltration detection. Triggers: 'data exfiltration', 'data theft signals', 'DNS tunneling'. Not for: DLP product selection or insider-threat HR process."
metadata:
  skill_id: "skl_wojt8Z7UgarJf-JnUVc1mg"
  title: "data exfiltration\" signals to watch for"
  version: "skv_z1vIIqY_QstkkSTpgOHRLA"
  updated: "2026-10-04T12:57:29.952541+00:00"
  canonical_url: "https://vectle.com/skills/skl_wojt8Z7UgarJf-JnUVc1mg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

# "data exfiltration" signals to watch for

## TL;DR
Exfiltration looks like normal traffic, just more of it or at stranger hours. Watch for big outbound transfers to places you dont normally send data, DNS queries shaped like tunnels, and uploads to personal cloud storage. When you spot one, the questions are who moved what, where it went, and how much, in that order.

```text
"data exfiltration" signals to watch for
```

## Use this when
- you suspect data theft by an outsider or an insider
- you are building exfiltration detection rules
- an alert fired on unusual outbound traffic
- you need to scope how much data left during an incident

## Not for this skill when
- you are selecting a DLP product (that is a buying decision)
- you need the HR and legal side of an insider case (get counsel involved)
- the "exfiltration" is a sanctioned migration or backup (verify first)
- you want packet-level forensics (that is a deeper skill)

## Steps
1. Watch outbound volume by host and user. A workstation suddenly uploading gigabytes, or a server talking to an IP it never talked to before, is the classic signal. Baseline first so you know what "suddenly" means for each host.

2. Watch DNS. Long random-looking subdomains, high query volumes to a single domain, and TXT record queries from non-mail hosts all suggest tunneling:
```spl
index=dns
| stats count by query
| sort - count
| head 30
```
Expected: mostly content-delivery and software-update noise. Truly random-looking strings repeated thousands of times are not noise.

3. Watch cloud storage and sharing. Look for large downloads followed by uploads to personal cloud domains, new external sharing links on sensitive files, and object-read spikes from a single principal in your cloud storage.

4. Watch the clock. Big transfers at 3am from an account that works 9 to 5 deserve a look even if the destination seems normal. Time-of-day is a weak signal alone but a strong one combined with volume.

5. Confirm before accusing. Check whether the transfer was a sanctioned backup, a migration, or an engineer doing something reasonable. Then check with the user or their manager. Exfiltration accusations are career-altering; be sure.

6. If it is real, preserve the logs first (see the log-preservation skill), then contain the account, then scope exactly what left. The scope decides notification duties, so "everything in that folder" is not an answer; file lists are.

### Variant: exfiltration through sanctioned tools
Attackers and insiders both abuse corporate file sharing, email, and chat. Watch for sharing-link creation on sensitive files, large attachments to personal addresses, and API-based bulk downloads through sanctioned apps.

### Variant: exfiltration via email
Large or numerous attachments to personal addresses, auto-forwarding rules to external mailboxes, and mailbox export requests are the email-shaped version. The mail gateway logs tell this story.

### Variant: slow-drip exfiltration under volume thresholds
Patient actors move a little data at a time to stay under alerts. Look at cumulative totals over weeks instead of daily spikes, and watch for regular small transfers to the same destination.

## Why this happens
Attackers and insiders both need to move data out, and the network is where that movement is visible. Most exfil goes out over the same protocols as normal work, HTTPS, DNS, email, which is why the signals are about volume, timing, and destination rather than protocol.

## Edge cases and pitfalls
- Encrypted traffic hides content, so you work with volume, timing, and destination, not payload. Accept that and build detections accordingly.
- CDNs and software updates create huge benign transfers. Baseline first or every patch Tuesday looks like an incident.
- Personal cloud use may violate policy without being exfiltration. Keep the response proportional until you know what moved.
- Data staging is a strong precursor signal. Watch for large archives being created or files being compressed before anything moves; that is the step before the transfer.
- Dont confront the user before you have the scope. If it is an insider, a warning gives them time to cover tracks; if it isnt, you just accused an innocent person.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_gaCZoXjjbs3E_l0LP0OITA


---

Source: [Vectle](https://vectle.com/skills/skl_wojt8Z7UgarJf-JnUVc1mg). Version: `skv_z1vIIqY_QstkkSTpgOHRLA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

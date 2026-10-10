---
name: "ansible-10-11-6-003bd2ec1508b783"
description: "Shows how to fix ansible + 10.11.6. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_5gu9IeScqi_-E73m89MDNw"
  title: "Ansible + 10.11.6"
  version: "skv_WW781CIzDrDa4tQxAfvpUA"
  updated: "2026-10-04T03:42:22.52416+00:00"
  canonical_url: "https://vectle.com/skills/skl_5gu9IeScqi_-E73m89MDNw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

The ansible documentation suggests doing this for every host by hand: ansible myhost --sudo -m raw -a "yum install -y python2 python-simplejson" However I think it's nicer to bootstrap all of your hosts with this snippet at the start of you playbook: - name: Bootrstrap python hosts: YOUR_HOST tasks: raw: sudo apt-get update && sudo apt-get -y python-simplejson delegate_to: '{{ item }}' with_items: {{ groups["hosts"] }} Context: Stack Overflow #38799807 (top answer, 5 votes, 3 answers): I'm having a weird issue with Ansible on a (very) clean install of 10.11.6.

## Steps

1. [zabeltech (top answer)] This happens if there is no python installed on the remote hosts. The ansible documentation suggests doing this for every host by hand: ansible myhost --sudo -m raw -a "yum install -y python2 python-simplejson" However I think it's nicer to bootstrap all of your hosts with this snippet at the start of you playbook: - name: Bootrstrap python hosts: YOUR_HOST tasks: raw: sudo apt-get update && sudo apt-get -y python-simplejson delegate_to: '{{ item }}' with_items: {{ groups["hosts"] }}

## When to use

You are seeing this: I then went to a preexisting (and crazy simple) Ansible project and did an... ansible -m ping all It then asked me to enter my SSH passphrase. Use this skill when you run into "Ansible + 10.11.6".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 10.11.6. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_5gu9IeScqi_-E73m89MDNw). Version: `skv_WW781CIzDrDa4tQxAfvpUA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

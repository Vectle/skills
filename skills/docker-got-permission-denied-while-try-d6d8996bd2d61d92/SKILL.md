---
name: "docker-got-permission-denied-while-try-d6d8996bd2d61d92"
description: "Shows how to fix docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_5vTaXqVsBM_ipODSoi4_bg"
  title: "Docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock"
  version: "skv_nJf68SAXku0ayRlEB-FRgQ"
  updated: "2026-10-04T06:17:27.838197+00:00"
  canonical_url: "https://vectle.com/skills/skl_5vTaXqVsBM_ipODSoi4_bg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

I just tried to use docker in my local machine(Ubuntu 16.04) with Jenkins.

## Steps

1. If using jenkins The user jenkins needs to be added to the group docker : sudo usermod -a -G docker jenkins Then restart Jenkins. Otherwise If you arrive to this question of stack overflow because you receive this message from docker, but you don't use jenkins, most probably the error is the same: your unprivileged user does not belong to the docker group. You can do: sudo usermod -a -G docker $USER You can check it was successful by doing grep docker /etc/group and see something like this: docker:x:998:[user] in one of the lines. Then change your users group ID to docker (to avoid having to log out and log in again): newgrp docker

## When to use

You are seeing this: You can do: sudo usermod -a -G docker $USER You can check it was successful by doing grep docker /etc/group and see something like this: docker:x:998:[user] in one of the lines. Use this skill when you run into "Docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: docker.imagemaven 3.3.3. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_5vTaXqVsBM_ipODSoi4_bg). Version: `skv_nJf68SAXku0ayRlEB-FRgQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

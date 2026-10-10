---
name: "bug-report-novu-application-getting-ne-a07935826ba09310"
description: "Shows how to fix \ud83d\udc1b Bug Report: Novu Application getting Network Error while getting singup. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_wtiXgq4Af4oXexkJLMzI9Q"
  title: "\ud83d\udc1b Bug Report: Novu Application getting Network Error while getting singup"
  version: "skv_PtFyqbxZEYOdSPLliX8AkQ"
  updated: "2026-10-03T22:26:16.432078+00:00"
  canonical_url: "https://vectle.com/skills/skl_wtiXgq4Af4oXexkJLMzI9Q"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

We have using ingress AWS ALB to expose novu application to public. my env-dev file is 👍 # Secrets # YOU MUST CHANGE THESE BEFORE GOING INTO PRODUCTION JWT_SECRET [redacted] STORE_ENCRYPTION_KEY [redacted] ## General NODE_ENV=production MONGO_URL=XXXXX/novu-db MONGO_MAX_POOL_SIZE=500 REDIS_HOST=novu-redis-dev #REDIS_CACHE_SERVICE_HOST=novu-redis-dev #REDIS_CACHE_SERVICE_PORT=6379 # AWS...

## Steps

1. If self-hosted Novu shows network errors on signup or signin after you changed API_ROOT_URL, note that Novu writes REACT_APP_API_URL into MongoDB on first start, so later env changes have no effect (the volume survives docker-compose down). One user fixed it by tearing down, removing the mongodb volume, and starting again with the correct .env. If you are on Kubernetes with an ingress, another user fixed the same symptom by stripping the /api prefix in the ingress rewrite so the API service receives paths like /v1/auth.

## When to use

You are seeing this: Issue novuhq/novu#3602 (closed, 36 comments): ### 📜 Description We have deployed novu in Kubernetes environment with provided kustomize deployments files in Novu Documentation. we have facing issue(Network Issue) while getting signup or Sign in to Novu. Use this skill when you run into "🐛 Bug Report: Novu Application getting Network Error while getting singup".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_wtiXgq4Af4oXexkJLMzI9Q). Version: `skv_PtFyqbxZEYOdSPLliX8AkQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

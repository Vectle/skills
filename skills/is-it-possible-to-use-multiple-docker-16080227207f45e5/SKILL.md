---
name: "is-it-possible-to-use-multiple-docker-16080227207f45e5"
description: "Guide Is it possible to use multiple docker images in bitbucket pipeline?: Like that: [code: pipelines: default: - step: name: Build and test image: node:8.6 script: - npm install - npm test - npm run build artifacts: - dist/** - step: name: Deploy image: python:3.5. Use this when you hit exactly this in Is. Not for different errors or different tools."
metadata:
  skill_id: "skl_swz2VRtUbycrOiVnFgvFzA"
  title: "Is it possible to use multiple docker images in bitbucket pipeline?"
  version: "skv_sg-4HMF9HbrJdZiad3dKCg"
  updated: "2026-10-03T05:30:56.514088+00:00"
  canonical_url: "https://vectle.com/skills/skl_swz2VRtUbycrOiVnFgvFzA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Like that: [code: pipelines: default: - step: name: Build and test image: node:8.6 script: - npm install - npm test - npm run build artifacts: - dist/** - step: name: Deploy image: python:3.5.1 trigger: manual script: - python deploy.py ] You can specify an image for each step.

## Fix
1. Like that: [code: pipelines: default: - step: name: Build and test image: node:8.6 script: - npm install - npm test - npm run build artifacts: - dist/** - step: name: Deploy image: python:3.5.1 trigger: manual script: - python deploy.py ].
   Expected: this specific failure stops.

## Details
You can specify an image for each step.

## When to use
You hit exactly this: Is it possible to use multiple docker images in bitbucket pipeline? in Is.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Is (versions mentioned here: 8.6, 3.5.1).

---

Source: [Vectle](https://vectle.com/skills/skl_swz2VRtUbycrOiVnFgvFzA). Version: `skv_sg-4HMF9HbrJdZiad3dKCg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

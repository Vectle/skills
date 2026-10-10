---
name: "custom-auth-flow-with-bad-answer-infin-064a51a3f003f772"
description: "Shows how to fix custom Auth Flow With Bad Answer Infinite Loop. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_sQrYDKQVlLl977ocPwEP2Q"
  title: "Custom Auth Flow With Bad Answer Infinite Loop"
  version: "skv_GRQHPJSWMFgZRnPsVH3MJA"
  updated: "2026-10-04T05:41:38.702159+00:00"
  canonical_url: "https://vectle.com/skills/skl_sQrYDKQVlLl977ocPwEP2Q"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

What was reported: Issue aws-samples/amazon-cognito-passwordless-auth#208 (closed, 6 comments): Hi guys, I've been fiddling around with this package and I don't know how to handle the error when a bad code is submitted since the auth flow just loops infinitely here's my pseudo example in Angular. ``` import { Component, OnInit, ViewEncapsulation, EventEmitter } from '@angular/core'; import { Passwordless } from "amazon-cognito-passwordless-auth"; import { authenticateWithSRP } from "amazon-cognito-passwordless-auth/srp"; export class LoginComponentComponent implements OnInit { myPromise: Promi

## Steps

1. What was reported:
Issue aws-samples/amazon-cognito-passwordless-auth#208 (closed, 6 comments): Hi guys, I've been fiddling around with this package and I don't know how to handle the error when a bad code is submitted since the auth flow just loops infinitely here's my pseudo example in Angular. ``` import { Component, OnInit, ViewEncapsulation, EventEmitter } from '@angular/core'; import { Passwordless } from "amazon-cognito-passwordless-auth"; import { authenticateWithSRP } from "amazon-cognito-passwordless-auth/srp"; export class LoginComponentComponent implements OnInit { myPromise: Promise[string] constructor() { } ngOnInit() { Passwordless.configure({ userPoolId: environment.

2. What works:
In a custom auth flow, the function you pass to customChallengeAnswer is invoked every time a custom answer is needed. If it doesn't return a fresh promise on each invocation, the challenge resolves immediately with the old (wrong) value and the flow loops forever when a bad code is submitted. Fix: make sure customChallengeAnswer returns a new promise every time it's called, so a wrong code produces a proper retry or error instead of looping.

## When to use

Use this skill when you run into "Custom Auth Flow With Bad Answer Infinite Loop".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_sQrYDKQVlLl977ocPwEP2Q). Version: `skv_GRQHPJSWMFgZRnPsVH3MJA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

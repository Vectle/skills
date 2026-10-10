---
name: "semgrep-not-finding-two-lines-of-code-4fc5006d16b89601"
description: "Shows how to fix semgrep not finding two lines of code with a 'patterns' section. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_sQJxZvhhQT8O3_7zeQq_Sw"
  title: "Semgrep not finding two lines of code with a 'patterns' section"
  version: "skv_RnBrut_ea8oDO6ksdS8zqg"
  updated: "2026-10-04T08:15:20.138341+00:00"
  canonical_url: "https://vectle.com/skills/skl_sQJxZvhhQT8O3_7zeQq_Sw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

[bstpierre (top answer)] Using pattern-inside works: `` rules: - id: chat patterns: - pattern-inside: | var $X = GrpcChannel.ForAddress(...);... - pattern: var $Y = new ChatService.ChatServiceClient($X); languages: - csharp message: [pass] severity: INFO ` with this test case: ` using Grpc.Net.Client; using GrpcChat.ProtoBuf; var channel = GrpcChannel.ForAddress("YOUR\_HOST (port 8888)"); // ruleid: chat var client = new ChatService.ChatServiceClient(channel); ` when I run a test: ` % semgrep --test rules/ ✓ All tests passed! ` Context: Stack Overflow #71459777 (top answer, 4 votes, 1 answers)

## Steps

1. [bstpierre (top answer)] Using pattern-inside works:

``` rules: - id: chat patterns: - pattern-inside: | var $X = GrpcChannel.ForAddress(...); ... - pattern: var $Y = new ChatService.ChatServiceClient($X); languages: - csharp message: [pass] severity: INFO ```

``` using Grpc.Net.Client; using GrpcChat.ProtoBuf; var channel = GrpcChannel.ForAddress("YOUR_HOST (port 8888)"); // ruleid: chat var client = new ChatService.ChatServiceClient(channel); ```

``` % semgrep --test rules/ ✓ All tests passed! ```

``` rules: - id: create-chat-client patterns: - pattern: var $X = GrpcChannel.ForAddress(...); - pattern: var $Y = new ChatService.ChatServiceClient($X); languages: - csharp message: [pass] severity: INFO ```

2. And I am trying to match this code:

``` using Grpc.Net.Client; using GrpcChat.ProtoBuf; var channel = GrpcChannel.ForAddress("YOUR_HOST (port 8888)"); var client = new ChatService.ChatServiceClient(channel); ```

3. These match separately, but the 'patterns' should be a "AND" match and it fails. I must be missing something o

## When to use

You are seeing this: I must be missing something o Use this skill when you run into "Semgrep not finding two lines of code with a 'patterns' section".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_sQJxZvhhQT8O3_7zeQq_Sw). Version: `skv_RnBrut_ea8oDO6ksdS8zqg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

---
name: "international-model-studio-api-keys-re-37baaf7705cc1ba9"
description: "International Model Studio API keys return 401 with current fixed endpoints: : Fixed and merged: #45 (merge commit `62be239`, `main` CI green on all four legs)."
metadata:
  skill_id: "skl_g4FfISRIC_QSAlH2Nv6d6g"
  title: "International Model Studio API keys return 401 with current fixed endpoints"
  version: "skv_k0S8JgmJydFnP16Fb9fyXg"
  updated: "2026-10-08T14:54:30.048824+00:00"
  canonical_url: "https://vectle.com/skills/skl_g4FfISRIC_QSAlH2Nv6d6g"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

[nixi-agent]: Fixed and merged: #45 (merge commit `62be239`, `main` CI green on all four legs). **What changed** , the endpoints are no longer hard-coded per module. `session.base_url` is now the single source of truth: the text-translation (`/compatible-mode/v1/chat/completions`) and TTS (`/api/v1/services/aigc/multimodal-generation/generation`) endpoints derive their **host** from it, so one `base_url` drives all three legs. (The module constants stay only as function defaults, for callers outside the app.) **Alibaba Cloud Model Studio (international) is now a built-in line**, with the region picker asked for in the comment above: - `session.provider: qianwen | bailian_intl` - host template `wss://{workspace_id}.{region}.maas.aliyuncs.com/api-ws/v1/realtime` - regions: `ap-southeast-1` (Singapore, default) / `ap-northeast-1` (Tokyo) / `us-east-1` (Virginia) / `eu-central-1` (Frankfurt) / `cn-hongkong` - GUI: `Settings → General → Service Line` + Workspace ID (= the API Host prefix from the console, e.g. `llm-xxxx`) + Region. Keys are stored **per line**, so switching lines does not require re-entering the key. - The 401 in the report came from the voice-preview leg (the TTS/multimodal endpoint). That leg now uses the selected line's endpoint as well , which is why the same key previously failed while the realtime leg looked fine. Docs (all five languages) now walk through the

Context: GitHub issue nixi-agent/vrchat-livetranslate#43 (closed, 2 comments, reported 2026-10-01): ## Problem Overseas users using an Alibaba Cloud / Model Studio international API key can fail with `HTTP 401 invalid_api_key` when VRChat LiveTranslate calls the currently configured endpoints. Observed log: ```text 01:05:15.691 [config] API key 来源：界面保存（sk-****_K-I（114 字符）） 01:05:15.692 [gui] 试听音色 → 'Tina'（speech，模型 qwen3-tts-flash） 01:05:15.981 [gui] 试听失败（'Tina'）：HTTP 401：{"error":{"message":"Invalid API-key provided. For details, see: https://www.alibabacloud.com/help/en/model-studio/error-code#apikey-error","id":"b7533dab-dc56-9fbf-96a4-7bb62bca25c3","type":"invalid_request_error","code

## Matched source
Source: GitHub issue: https://github.com/nixi-agent/vrchat-livetranslate/issues/43
Original query: "International Model Studio API keys return 401 with current fixed endpoints"
Key terms: current, endpoints, fixed, international, keys, model, return, studio


---

Source: [Vectle](https://vectle.com/skills/skl_g4FfISRIC_QSAlH2Nv6d6g). Version: `skv_k0S8JgmJydFnP16Fb9fyXg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

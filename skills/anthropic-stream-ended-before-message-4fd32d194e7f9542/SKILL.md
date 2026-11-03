---
name: "anthropic-stream-ended-before-message-4fd32d194e7f9542"
description: "anthropic stream ended before message_stop error"
metadata:
  skill_id: "skl_bWupnLxkTyz3poEVwPhwHg"
  title: "anthropic stream ended before message_stop error"
  version: "skv_22Xkg_fSIv7OKJtM4jiduQ"
  updated: "2026-11-03T01:56:59.729658+00:00"
  canonical_url: "https://vectle.com/skills/skl_bWupnLxkTyz3poEVwPhwHg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Log the last event received.** Instrument the stream loop to record the type of every event and print the last one before the close. Expected: you see where the cut happened, usually after content_block_delta events during a long generation, or right after an error event.

**Check for a mid-stream error event.** Look for an error event in the stream, for example an overloaded_error or an api_error sent after the response started. Success check: if an error event is present, the API did report the failure in-band; surface that error in your code instead of the generic stream-ended message, and retry with exponential backoff.

**Test the same request without your proxy in the path.** Run the identical streaming request from a direct connection, bypassing any reverse proxy, corporate gateway, or serverless edge layer. Expected: if the direct stream reaches message_stop, an idle timeout or response buffering setting in the middle layer is closing long-lived SSE connections; raise its idle timeout and disable response buffering for the streaming route.

**Raise the client timeout and keep retries on.** Use the SDK default timeout or a longer one for streaming calls, not a short REST-style timeout, and leave the SDK max retries enabled so transient closes are retried automatically. Success check: a deliberately long generation completes and the stream ends with a message_delta carrying the stop reason, followed by message_stop.

**Handle a cut stream as a failed request.** In your own stream consumer, raise or return an error when the connection closes before message_stop, and retry the full request with backoff and jitter rather than appending to the partial text. Success check: a simulated mid-stream disconnect produces one clean retried response, never a half answer presented as complete.

---

Source: [Vectle](https://vectle.com/skills/skl_bWupnLxkTyz3poEVwPhwHg). Version: `skv_22Xkg_fSIv7OKJtM4jiduQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

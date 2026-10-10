---
name: "pub-sub-python-publisher-futures-batch-d13979d8b78c6f5e"
description: "Shows how to fix pub/Sub Python publisher: futures, batching, and ordering keys. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_hzLwpX68f-FeHFIlbrU1ig"
  title: "Pub/Sub Python publisher: futures, batching, and ordering keys"
  version: "skv_KkoLIV1AfmXtMADBjmodYA"
  updated: "2026-10-03T14:14:06.649662+00:00"
  canonical_url: "https://vectle.com/skills/skl_hzLwpX68f-FeHFIlbrU1ig"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Enable it at topic creation; you cannot retrofit ordering onto an existing topic without recreating it. Always call future.result() (with a timeout) or add a done callback, or your process can exit before anything is published.

```text
from google.cloud import pubsub_v1
publisher = pubsub_v1.PublisherClient()
topic = publisher.topic_path("[PROJECT-ID]", "[TOPIC]")
future = publisher.publish(topic, b"hello", origin="agent")
message_id = future.result(timeout=30)
print(message_id)
```

## Steps

1. ```python
from google.cloud import pubsub_v1
publisher = pubsub_v1.PublisherClient()
topic = publisher.topic_path("[PROJECT-ID]", "[TOPIC]")
future = publisher.publish(topic, b"hello", origin="agent")
message_id = future.result(timeout=30)
print(message_id)
```

2. publish() is async. It returns a future; the message is not sent until the batch flushes. Always call future.result() (with a timeout) or add a done callback, or your process can exit before anything is published. This is the number one Pub/Sub bug in agent-written scripts.

3. Ordering keys: pass ordering_key [your value] to publish, but the topic MUST have message ordering enabled first. If it is not enabled, publishing with an ordering key errors. Enable it at topic creation; you cannot retrofit ordering onto an existing topic without recreating it.

4. Batching: the default batch settings (up to 100 messages or 1MB or 10ms... check current defaults) suit throughput. For latency-sensitive flows, shrink max_latency.

5. Attributes vs data URIs message data is bytes; put routing metadata in attributes (string key/value pairs) so subscribers can filter without parsing the body.

6. Exactly-once is a subscription property, not a publisher property, and it costs latency. Do not promise exactly-once from the publisher side.

7. Regional endpoints: publishing to a topic in another region works but adds latency; keep publishers near their topics.

8. Verify: publish one message, then pull it with a test subscription or check the topic's sent-message count in the console. Confirm ordering behavior with two messages sharing a key.

## When to use

You are seeing this: ``python from google.cloud import pubsub\_v1 publisher = pubsub\_v1.PublisherClient() topic = publisher.topic\_path("[PROJECT-ID]", "[TOPIC]") future = publisher.publish(topic, b"hello", origin="agent") message\_id = future.result(timeout=30)... Use this skill when you run into "Pub/Sub Python publisher: futures, batching, and ordering keys".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_hzLwpX68f-FeHFIlbrU1ig). Version: `skv_KkoLIV1AfmXtMADBjmodYA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

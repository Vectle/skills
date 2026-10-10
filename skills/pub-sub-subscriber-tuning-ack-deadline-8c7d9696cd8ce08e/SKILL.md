---
name: "pub-sub-subscriber-tuning-ack-deadline-8c7d9696cd8ce08e"
description: "Shows how to fix pub/Sub subscriber tuning: ack deadlines, flow control, and redelivery. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_dqCctG7ii3bhmzRsYeaggg"
  title: "Pub/Sub subscriber tuning: ack deadlines, flow control, and redelivery"
  version: "skv_isx7pX3ozbm8J_dyYktdBg"
  updated: "2026-10-03T14:05:19.57205+00:00"
  canonical_url: "https://vectle.com/skills/skl_dqCctG7ii3bhmzRsYeaggg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Set max_messages (and max_bytes) to what your handler concurrency can actually drain. Fix: set the subscription ack deadline up to 600 seconds to cover your p99 handler time, or use exactly-once with lease management.

## Steps

1. ```python
from google.cloud import pubsub_v1
subscriber = pubsub_v1.SubscriberClient()
sub = subscriber.subscription_path("[PROJECT-ID]", "[SUB]")
flow = pubsub_v1.types.FlowControl(max_messages=50)
streaming_pull = subscriber.subscribe(sub, callback=handle, flow_control=flow)
```

2. What agents get wrong:

3. Ack deadline. The default is 10 seconds. If your handler takes 60 seconds, the message redelivers while you are still working and you process it twice (or ten times). Fix: set the subscription ack deadline up to 600 seconds to cover your p99 handler time, or use exactly-once with lease management. The client library can extend leases automatically while the handler runs, but only if you use the streaming pull subscriber, not manual pull loops.

4. Flow control. Without it, the subscriber happily buffers thousands of messages and OOMs your container. Set max_messages (and max_bytes) to what your handler concurrency can actually drain.

5. Ack vs nack. Ack on success. Nack (or let it expire) on transient failure so it redelivers. On permanent failure (poison message), ack it and route to a dead-letter topic, or it retries forever. Configure a dead-letter topic with max_delivery_attempts on the subscription.

6. Exactly-once delivery is a subscription setting with real latency cost. Most agent workloads are fine with at-least-once plus idempotent handlers. Make your handler idempotent (dedupe on message_id) instead of paying for exactly-once.

7. Push vs pull: if your subscriber is Cloud Run, consider a push subscription with OIDC auth instead of running a pull loop in the container.

8. Verify: publish test messages, watch acked vs redelivered counts in Cloud Monitoring, and confirm no duplicate processing in your logs.

## When to use

You are seeing this: ``python from google.cloud import pubsub\_v1 subscriber = pubsub\_v1.SubscriberClient() sub = subscriber.subscription\_path("[PROJECT-ID]", "[SUB]") flow = pubsub\_v1.types.FlowControl(max\_messages=50) streaming\_pull = subscriber.subscribe(sub,... Use this skill when you run into "Pub/Sub subscriber tuning: ack deadlines, flow control, and redelivery".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_dqCctG7ii3bhmzRsYeaggg). Version: `skv_isx7pX3ozbm8J_dyYktdBg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

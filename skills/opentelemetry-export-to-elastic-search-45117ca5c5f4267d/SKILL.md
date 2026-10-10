---
name: "opentelemetry-export-to-elastic-search-45117ca5c5f4267d"
description: "OpenTelemetry Export to Elastic Search without Elastic APM: After trying this for some time, I've finally made it to work with the latest version of opentelemetry-collector-contrib (0.60.0 at the time of this writting). Use when hitting this exact issue. Not for unrelated errors."
metadata:
  skill_id: "skl_9S2IdapAs8P9NOloBsg0Dw"
  title: "OpenTelemetry Export to Elastic Search without Elastic APM"
  version: "skv_JcsE3p3elxeDmqtgZR15JQ"
  updated: "2026-10-03T14:03:40.689174+00:00"
  canonical_url: "https://vectle.com/skills/skl_9S2IdapAs8P9NOloBsg0Dw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

I also had to follow the instructions to set the vm.max_map_count to at least 262144. Then, using the same net, I started an opentelemetry-collector-contrib docker image using a command like: docker run --net certs_default --name opentelemetry-collector -v C:\docker\elastic\otel-collector-config.mount the host path yaml at container path /etc/otelcol-contrib/config.yaml -p 4317:4317 -p 4318:4318 otel/opentelemetry-collector-contrib:0.60.0 The configuration file is very simple: receivers: otlp: protocols: grpc: http: exporters: logging: loglevel: debug elasticsearch/trace: endpoints: [a local/non-public address] user: elastic password - api_key - tls: insecure_skip_verify: true service: pipelines: traces: receivers: [otlp] exporters: [elasticsearch/trace] Finally, I've just configured my application to use the OtlpExporter: .AddOtlpExporter(configure =&gt; { configure.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.Grpc; }) Doing these steps, I can see my traces in Kibana. After trying this for some time, I've finally made it to work with the latest version of opentelemetry-collector-contrib (0.60.0 at the time of this writting).

After trying this for some time, I've finally made it to work with the latest version of opentelemetry-collector-contrib (0.60.0 at the time of this writting). First I've created a multi-node cluster with Docker Compose using the steps here https://www.elastic.co/guide/en/elasticsearch/reference/8.4/docker.html#docker-compose-file . I also had to follow the instructions to set the vm.max_map_count to at least 262144. Then, using the same net, I started an opentelemetry-collector-contrib docker image using a command like: docker run --net certs_default --name opentelemetry-collector -v C:\docker\elastic\otel-collector-config.mount the host path yaml at container path /etc/otelcol-contrib/config.yaml -p 4317:4317 -p 4318:4318 otel/opentelemetry-collector-contrib:0.60.0 The configuration file is very simple: receivers: otlp: protocols: grpc: http: exporters: logging: loglevel: debug elasticsearch/trace: endpoints: [a local/non-public address] user: elastic password - api_key - tls: insecure_skip_verify: true service: pipelines: traces: receivers: [otlp] exporters: [elasticsearch/trace] Finally, I've just configured my application to use the OtlpExporter: .AddOtlpExporter(configure =&gt; { configure.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.Grpc; }) Doing these steps, I can see my traces in Kibana. Now it would be nice to have some template to display a single trace with all the spans.

Context: I'd like to export trace/metrics data to Elastic Search using OpenTelemetry, but I'd prefer to avoid Elastic APM. Is it possible? The opentelemetry contrib repo apparently suggests it is possible, however, I did not find anything on elastic.co documentation. By the way, openapm.io implies see here , OpenTelemetry can export to elastic beats (which is extremely desirable), but again, I did not find anything in Elastic.co docs.

## Matched source
Source: Source: https://stackoverflow.com/questions/70909613/opentelemetry-export-to-elastic-search-without-elastic-apm
Original query: "OpenTelemetry Export to Elastic Search without Elastic APM"
Key terms: elastic, export, opentelemetry, search, without

## When to use

- You hit this exact issue.
- The symptom matches: OpenTelemetry Export to Elastic Search without Elastic APM.

## When NOT to use

- A different error or symptom; the cause here is specific to this one.

## Compatibility

Per the linked source (mentions 0.60.0, 8.4).

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://stackoverflow.com/questions/70909613/opentelemetry-export-to-elastic-search-without-elastic-apm

---

Source: [Vectle](https://vectle.com/skills/skl_9S2IdapAs8P9NOloBsg0Dw). Version: `skv_JcsE3p3elxeDmqtgZR15JQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

---
name: "how-to-configure-apm-server-to-docker-b84ea037b566d110"
description: "How to configure APM server to docker-compose file. You need to add APM to your docker file like this: apm-server: image: docker.elastic.co/apm/apm-server:7.13.0 cap_add: [\"CHOWN\", \"DAC_OVERRIDE\", \"SETGID\", \"SETUID\"] cap_drop: [\"ALL\"] ports: - 8200:8200 command: &gt; apm-server -e -E apm-server.rum.enabled=true -E setup.kibana.host=kibana:5601 -E setup.template.settings.index.number_of_replicas=0 -E apm-server.kibana.enabled=true -E apm-server.kibana.host=kibana:5601 -E output.elasticsearch.host"
metadata:
  skill_id: "skl_Y--hyFau-54mv8tL895iVg"
  title: "How to configure APM server to docker-compose file"
  version: "skv_kPI89BlthQ8vv-0Gccv4cQ"
  updated: "2026-10-03T14:02:15.295903+00:00"
  canonical_url: "https://vectle.com/skills/skl_Y--hyFau-54mv8tL895iVg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

You need to add APM to your docker file like this: apm-server: image: docker.elastic.co/apm/apm-server:7.13.0 cap_add: ["CHOWN", "DAC_OVERRIDE", "SETGID", "SETUID"] cap_drop: ["ALL"] ports: - 8200:8200 command: &gt; apm-server -e -E apm-server.rum.enabled=true -E setup.kibana.host=kibana:5601 -E setup.template.settings.index.number_of_replicas=0 -E apm-server.kibana.enabled=true -E apm-server.kibana.host=kibana:5601 -E output.elasticsearch.hosts=["elasticsearch:9200"] healthcheck: interval: 10s retries: 12 test: curl --write-out 'HTTP %{http_code}' --fail --silent --output /dev/null a local/non-public address/ (port 8200)

## Fix

1. You need to add APM to your docker file like this: apm-server: image: docker.elastic.co/apm/apm-server:7.13.0 cap_add: ["CHOWN", "DAC_OVERRIDE", "SETGID", "SETUID"] cap_drop: ["ALL"] ports: - 8200:8200 command: &gt; apm-server -e -E apm-server.rum.enabled=true -E setup.kibana.host=kibana:5601 -E setup.template.settings.index.number_of_replicas=0 -E apm-server.kibana.enabled=true -E apm-server.kibana.host=kibana:5601 -E output.elasticsearch.hosts=["elasticsearch:9200"] healthcheck: interval: 10s retries: 12 test: curl --write-out 'HTTP %{http_code}' --fail --silent --output /dev/null a local/non-public address/ (port 8200)
   Expected: You see the expected output instead of the problem.

## When to use

- You are dealing with this situation.
- The symptom matches: How to configure APM server to docker-compose file.

## When NOT to use

- Unrelated issues with a different cause.
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported per the linked source (mentions 3.8, 7.13.0). Source: https://stackoverflow.com/questions/67791781/how-to-configure-apm-server-to-docker-compose-file.

## Variant phrasings

### How to configure APM server to docker-compose file

## Why it happens

I have a docker-compose.yml file that consists of elasticsearch & kibana. I am wanting to add the APM Server service in the docker-compose.yml file. Is there a way to configure the apm server to the .yml file? I was reading up on configuring apm server on docker but this is not what I am looking for since I am doing this with docker-compose. My docker-compose file: version: '3.8' services: elasticsearch: container_name: elasticsearch image: docker.elastic.co/elasticsearch/ela

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- Behavior can change between releases; the linked source reflects the versions above.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://stackoverflow.com/questions/67791781/how-to-configure-apm-server-to-docker-compose-file

---

Source: [Vectle](https://vectle.com/skills/skl_Y--hyFau-54mv8tL895iVg). Version: `skv_kPI89BlthQ8vv-0Gccv4cQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

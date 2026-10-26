---
name: "cassandra-astra-securely-deploying-to-e8dd79303036b73e"
description: "Cassandra Astra securely deploying to heroku: If you can checkin secure bundle into repo, then it should be easy - you just need to point to it from the cloud config map, and take username/password from the configured secrets via environment variables: from cassandra.cluster import Cluster from cassandra.auth import PlainTextAuthProvider import os cloud_config = { 'secure_connect_bundle': '/path/to/secure-connect-dbname.zip' } auth_provider = PlainTextAuthProvider( username=os.environ['CASSANDRA"
metadata:
  skill_id: "skl_rwA0uIGRfBrftmYhmJHF1w"
  title: "Cassandra Astra securely deploying to heroku"
  version: "skv_WGKbfh5B8N9xYA7X_EvjEQ"
  updated: "2026-10-03T13:52:37.591872+00:00"
  canonical_url: "https://vectle.com/skills/skl_rwA0uIGRfBrftmYhmJHF1w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/62645124/cassandra-astra-securely-deploying-to-heroku\"]"
---

## TL;DR

If you can checkin secure bundle into repo, then it should be easy - you just need to point to it from the cloud config map, and take username/password from the configured secrets via environment variables: from cassandra.cluster import Cluster from cassandra.auth import PlainTextAuthProvider import os cloud_config = { 'secure_connect_bundle': '/path/to/secure-connect-dbname.zip' } auth_provider = PlainTextAuthProvider( username=os.environ['CASSANDRA_USERNAME'], password [your value] cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider) session = cluster.connect() Idea about storing the file on S3, and downloading - isn't very bad as well.

If you can checkin secure bundle into repo, then it should be easy - you just need to point to it from the cloud config map, and take username/password from the configured secrets via environment variables: from cassandra.cluster import Cluster from cassandra.auth import PlainTextAuthProvider import os cloud_config = { 'secure_connect_bundle': '/path/to/secure-connect-dbname.zip' } auth_provider = PlainTextAuthProvider( username=os.environ['CASSANDRA_USERNAME'], password [your value] cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider) session = cluster.connect() Idea about storing the file on S3, and downloading - isn't very bad as well. You can implement it in the script itself, to get file, and you can use environment variables to pass S3 credentials as well, so file won't be accessible in the repository, plus it would be easier to exchange the secure bundles if necessary.

Context: I am developing an app using python and Cassandra(Astra provider) and trying to deploy it on Heroku. The problem is connecting to the database requires the credential zip file to be present locally- https://docs.datastax.com/en/astra/aws/doc/dscloud/astra/dscloudConnectPythonDriver.html '/path/to/secure-connect-database_name.zip' and Heroku does not have support for uploading credentials files. I can configure the username and password as environment variable but the credenti

## Matched source
Source: Source: https://stackoverflow.com/questions/62645124/cassandra-astra-securely-deploying-to-heroku
Original query: "Cassandra Astra securely deploying to heroku"
Key terms: astra, cassandra, deploying, heroku, securely

## When to use

- You hit this exact issue.
- The symptom matches: Cassandra Astra securely deploying to heroku.

## When NOT to use

- A different error or symptom; the cause here is specific to this one.

## Compatibility

Per the linked source.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://stackoverflow.com/questions/62645124/cassandra-astra-securely-deploying-to-heroku

---

Source: [Vectle](https://vectle.com/skills/skl_rwA0uIGRfBrftmYhmJHF1w). Version: `skv_WGKbfh5B8N9xYA7X_EvjEQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

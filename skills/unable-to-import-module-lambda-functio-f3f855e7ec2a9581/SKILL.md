---
name: "unable-to-import-module-lambda-functio-f3f855e7ec2a9581"
description: "Fixes the AWS Lambda error where the function fails at import because boto3 is not in the deployment package. Use when a Lambda deploy or test event dies with this exact import error. Not for local boto3 installs or credential errors."
metadata:
  skill_id: "skl_i8gtV8vloRlUX3b8O9G6fQ"
  title: "Unable to import module 'lambda_function': No module named 'boto3'"
  version: "skv_Dawtdo3MCofZ3gsX11tyUg"
  updated: "2026-10-03T06:07:10.733935+00:00"
  canonical_url: "https://vectle.com/skills/skl_i8gtV8vloRlUX3b8O9G6fQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Your Lambda deployment package does not include boto3, and the Lambda Python runtime does not ship it either. Add boto3 with a Lambda layer or vendor it into your zip, then redeploy. Locally installed boto3 never reaches Lambda.

```text
Unable to import module 'lambda_function': No module named 'boto3'
```

## Fix it

1. Confirm the zip you upload actually lacks boto3: unzip -l your-function.zip | grep boto3. If nothing shows, that is the bug.
2. Easiest fix: attach a Lambda layer containing boto3. In the console go to your function, Layers, Add a layer, and pick an AWS-managed or community boto3 layer matching your Python runtime. Expected: the layer ARN appears under your function.
3. Or vendor it: pip install boto3 -t ./package, zip the contents of ./package plus your handler into the deployment zip. Expected: unzip -l shows boto3/ entries.
4. Redeploy and run a test event. Expected: no import error; the function runs.

## When this applies
- The error names lambda_function or your handler module and No module named 'boto3'.
- Code runs fine locally but fails in Lambda.

## When it doesn't
- The error happens on your laptop: that is a local pip/venv problem, not this.
- The error names a different missing module: fix that module the same way.

## Compatibility
- AWS Lambda Python 3.9 through 3.13 runtimes. boto3 any recent version.

## Why it happens
Lambda runs your code in a minimal runtime. Only the standard library plus a few AWS bits are present. boto3 is deliberately not preinstalled, so anything your handler imports must come from your zip or a layer.

## Edge cases
- If you need a newer boto3 than the layer provides, vendor it yourself; layers pin a version.
- Heavy zips (with numpy/pandas) can exceed the 250 MB unzipped limit; use layers to split it up.
- Same fix pattern applies to any third-party import failing in Lambda.


---

Source: [Vectle](https://vectle.com/skills/skl_i8gtV8vloRlUX3b8O9G6fQ). Version: `skv_Dawtdo3MCofZ3gsX11tyUg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

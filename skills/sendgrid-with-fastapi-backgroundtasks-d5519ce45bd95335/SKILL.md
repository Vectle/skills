---
name: "sendgrid-with-fastapi-backgroundtasks-d5519ce45bd95335"
description: "Send mail from FastAPI without slowing the endpoint: hand the send to BackgroundTasks, reuse one SendGrid client, and log SendGrid's error body on failure. Not the full reference manual."
metadata:
  skill_id: "skl_GAsKBWlK4lMkqWGsL7b-tw"
  title: "SendGrid with FastAPI: BackgroundTasks so mail does not block the response"
  version: "skv_DFIyTvuW5tWmyxLPIqYqbA"
  updated: "2026-10-03T05:35:37.333222+00:00"
  canonical_url: "https://vectle.com/skills/skl_GAsKBWlK4lMkqWGsL7b-tw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.sendgrid.com/api-reference/mail-send/mail-send\",\"https://github.com/sendgrid/docs/blob/develop/content/docs/for-developers/sending-email/quickstart-python.md\"]"
---

**TL;DR:** Send mail from FastAPI without slowing the endpoint: hand the send to BackgroundTasks, reuse one SendGrid client, and log SendGrid's error body on failure. BackgroundTasks run after the response goes out, so a slow SendGrid call never blocks the user. Create the client once at startup, not per request.

## The fix

import os, sendgrid
from fastapi import FastAPI, BackgroundTasks
from sendgrid.helpers.mail import Mail

app = FastAPI()
sg = sendgrid.SendGridAPIClient(api_key value os.environ.get('SENDGRID_API_KEY'))

def send_welcome(to_email: str):
  message = Mail(
    from_email='[YOUR_VERIFIED_SENDER]',  # verified sender
    to_emails=to_email,
    subject='Welcome',
    plain_text_content='Welcome aboard')
  response = sg.send(message)
  if response.status_code != 202:
    print('sendgrid failed', response.status_code, response.body)

@app.post('/signup')
def signup(email: str, background_tasks: BackgroundTasks):
  background_tasks.add_task(send_welcome, email)
  return {'ok': True}

Notes:
1. BackgroundTasks run after the response goes out, so a slow SendGrid call never blocks the user. But they die with the worker: for anything you cannot afford to lose, use a real queue.
2. Create the client once at startup, not per request.
3. Validate the email address in the endpoint; a 400 from SendGrid on a bad address is avoidable.
4. For tests, call the send function with sandbox mode enabled and assert 200.

## When to use this

- This covers exactly what the title says: SendGrid with FastAPI.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with SendGrid; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current SendGrid behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_GAsKBWlK4lMkqWGsL7b-tw). Version: `skv_DFIyTvuW5tWmyxLPIqYqbA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

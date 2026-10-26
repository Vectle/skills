---
name: "send-email-with-sendgrid-from-go-sendg-63571ea4ee95d0cd"
description: "The exact working pattern for sendgrid-go: mail helpers, NewSendClient from the environment, and reading StatusCode and Headers off the response. Not the full reference manual."
metadata:
  skill_id: "skl_lxy3SxAUTW5k45m6c4vHRg"
  title: "Send email with SendGrid from Go (sendgrid-go v3)"
  version: "skv_Ec2FqSVZBpQsSNcVboKfvw"
  updated: "2026-10-03T05:11:35.790961+00:00"
  canonical_url: "https://vectle.com/skills/skl_lxy3SxAUTW5k45m6c4vHRg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/sendgrid/docs/blob/develop/content/docs/for-developers/sending-email/quickstart-go.md\",\"https://github.com/sendgrid/sendgrid-go\",\"https://docs.sendgrid.com/api-reference/mail-send/mail-send\"]"
---

**TL;DR:** The exact working pattern for sendgrid-go: mail helpers, NewSendClient from the environment, and reading StatusCode and Headers off the response. Install: go get github.com/sendgrid/sendgrid-go. The from address must be a verified sender in the SendGrid account or the request fails.

## The fix

1. Install: go get github.com/sendgrid/sendgrid-go.

2. Build and send: import ( "fmt" "log" "os" "github.com/sendgrid/sendgrid-go" "github.com/sendgrid/sendgrid-go/helpers/mail" ) from := mail.NewEmail("Your Name", "[YOUR_VERIFIED_SENDER]") // verified sender to := mail.NewEmail("Their Name", "[RECIPIENT_EMAIL]") message := mail.NewSingleEmail(from, "subject here", to, "plain body", "[strong]html body[/strong]") client := sendgrid.NewSendClient(os.Getenv("SENDGRID_API_KEY")) response, err := client.Send(message) if err != nil { log.Println(err) } else { fmt.Println(response.StatusCode) // 202 means accepted fmt.Println(response.Headers) }

3. NewSingleEmail takes from, subject, to, plain text, html. For multi-recipient or per-recipient data, build the v3 JSON with the mail helpers instead.

4. The from address must be a verified sender in the SendGrid account or the request fails.

5. Keep SENDGRID_API_KEY in the environment. Do not hardcode it, and do not print the client config in logs.

## When to use this

- This covers exactly what the title says: Send email with SendGrid from Go (sendgrid-go v3).
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Send; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Send behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_lxy3SxAUTW5k45m6c4vHRg). Version: `skv_Ec2FqSVZBpQsSNcVboKfvw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

---
name: "send-email-with-sendgrid-from-php-send-668b95abc6ce7a4e"
description: "The exact working pattern for sendgrid-php: composer install, the Mail builder methods, and reading statusCode off the response inside a try/catch. Not the full reference manual."
metadata:
  skill_id: "skl_FDnhimSt6X-6x1DLJkq_zg"
  title: "Send email with SendGrid from PHP (sendgrid-php v8)"
  version: "skv_-ajWKmiPyuyolj_yYrClzw"
  updated: "2026-10-03T05:00:32.166057+00:00"
  canonical_url: "https://vectle.com/skills/skl_FDnhimSt6X-6x1DLJkq_zg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The exact working pattern for sendgrid-php: composer install, the Mail builder methods, and reading statusCode off the response inside a try/catch. Install: composer require sendgrid/sendgrid. Note the backslash-escaped class names (\SendGrid\Mail\Mail): inside double-quoted strings PHP would interpolate, so the quickstart uses single quotes and leading backslashes.

## The fix

1. Install: composer require sendgrid/sendgrid.

2. Build and send: require 'vendor/autoload.php'; use \SendGrid\Mail\Mail; $email = new Mail(); $email->setFrom('[YOUR_VERIFIED_SENDER]', 'Your Name'); // verified sender $email->setSubject('subject here'); $email->addTo('[RECIPIENT_EMAIL]', 'Their Name'); $email->addContent('text/plain', 'plain body'); $email->addContent('text/html', '[strong]html body[/strong]'); $sendgrid = new \SendGrid(getenv('SENDGRID_API_KEY')); try { $response = $sendgrid->send($email); printf("Response status: %d\n", $response->statusCode()); // 202 means accepted } catch (Exception $e) { echo 'Caught exception: ' . $e->getMessage() . "\n"; }

3. Note the backslash-escaped class names (\SendGrid\Mail\Mail): inside double-quoted strings PHP would interpolate, so the quickstart uses single quotes and leading backslashes.

4. The from address must be a verified sender or the send fails.

5. Read the key from the environment with getenv. Do not commit it, and do not echo it in error output.

## When to use this

- This covers exactly what the title says: Send email with SendGrid from PHP (sendgrid-php v8).
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Send; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Send behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_FDnhimSt6X-6x1DLJkq_zg). Version: `skv_-ajWKmiPyuyolj_yYrClzw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

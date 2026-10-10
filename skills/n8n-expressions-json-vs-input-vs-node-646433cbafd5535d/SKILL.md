---
name: "n8n-expressions-json-vs-input-vs-node-646433cbafd5535d"
description: "Shows how to fix n8n expressions: $json vs $input vs $('Node').item, paired-item gotchas and webhook response modes. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_t_E-6rEwgmRKW5MD1kRJWw"
  title: "n8n expressions: $json vs $input vs $('Node').item \u2014 paired-item gotchas and webhook response modes"
  version: "skv_JH7fXYl_o2SkMXgLrqT2VQ"
  updated: "2026-10-03T04:49:28.839085+00:00"
  canonical_url: "https://vectle.com/skills/skl_t_E-6rEwgmRKW5MD1kRJWw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Use "Immediately" for fire-and-forget, or "Using 'Respond to Webhook' Node" to reply early (for example a quick 202 ack) and keep processing after it. Also use this when configuring how a Webhook node replies to the caller. Use $('Node Name').first().json.FIELD. Replace.item with.first(),.last(), or.all()[INDEX].

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## n8n Expressions: `$json` vs `$input` vs `$('Node').item`, Paired-Item Gotchas and Webhook Response Modes

## When to use this

You are writing or debugging an n8n workflow and an expression returns `undefined`, the wrong row, or an error like `Multiple matching items for expression` or `Info for expression missing from previous node`. Also use this when configuring how a Webhook node replies to the caller.

## The three reference styles

| Style | What it resolves to | Scope |
|---|---|---|
| `{{ $json.field_name }}` | JSON data of the item currently being processed by THIS node. Shorthand for `{{ $input.item.json }}`. | Immediate predecessor's output only |
| `{{ $input.item.json.field_name }}` | The full current item (json + binary + metadata), then its JSON. | Immediate predecessor's output only |
| `{{ $('Node Name').item.json.field_name }}` | The item from the named node that is LINKED (paired) to the current item, item lineage, not "item 0". | Any named upstream node |

Expression-capable parameters accept `={{ ... }}`. A plain string that does not start with `=` is literal and is never evaluated.

## `$json` is the immediate predecessor's output, not "your data"

`$json` sees only what the node directly before this one emitted for this item. After a database node (Postgres insert, Supabase upsert, etc.), the item JSON is replaced by the DB row, fields produced further upstream become `undefined`.

Broken:

```
Set node "Set name from signup form":
  full_name = {{ $json.full_name }}
```

If a Postgres node ran between the signup Webhook node and the Set node, `$json.full_name` is undefined, the Postgres row has no `full_name`.

Fixed, reference the producing node explicitly:

```
full_name = {{ $('Webhook').first().json.full_name }}
```

Rule: once any transform, DB, HTTP, or aggregation node touches an item, reach back with `$('Node Name').first()` (literal first item) or `.item` (paired item) instead of `$json`.

## `$('Node').item` follows paired-item lineage, and aggregation breaks it

Each item n8n emits carries pairing info (`pairedItem`) recording which input item produced it. `$('Node Name').item` uses that lineage, so in a loop it tracks the matching row rather than always grabbing item 0. Use `.first()` when you genuinely want the literal first item of the named node.

## Gotcha 1: Code nodes break the lineage unless you return `pairedItem`

A Code node that returns brand-new items without pairing info breaks `$('Node').item` in downstream nodes with `Info for expression missing from previous node`. Fix it by returning which input item produced each output item:

```javascript
// Code node, "Run Once for Each Item"
return {
  json: {
    ...$input.item.json,
    total: $input.item.json.price * $input.item.json.qty
  },
  pairedItem: $itemIndex
};
```

For a one-to-many expansion:

```javascript
// Code node, "Run Once for All Items"
const out = [];
for (const [index, item] of $input.all().entries()) {
  for (const tag of item.json.tags) {
    out.push({ json: { tag }, pairedItem: index });
  }
}
return out;
```

## Gotcha 2: Aggregations throw `Multiple matching items for expression`

Summarize, Aggregate, and Merge nodes combine several input items into one output item. After them, `$('Upstream').item` is ambiguous, so n8n errors with `Multiple matching items for expression`. Resolve it explicitly:

```
{{ $('Webhook').first().json.full_name }}        // literal first
{{ $('Webhook').last().json.full_name }}         // literal last
{{ $('Webhook').all()[2].json.full_name }}       // by index
```

Or reference a node whose output still has one-to-one lineage with the current item.

## Gotcha 3: branches change what "current item" means

After an IF or Switch, `$json` in a downstream node only sees items that took that branch, and `$input.all()` returns only the items entering this node on this execution path. To compare across branches, use the Merge node to combine streams, or reference the named pre-branch node: `{{ $('Set Inputs').first().json.threshold }}`.

## `$input` helpers

```
{{ $input.all().length }}        // how many items entered this node
{{ $input.first().json.id }}     // first item of immediate predecessor
{{ $input.last().json.id }}      // last item
{{ $input.params.operation }}     // the previous node's configured operation
{{ $input.context.noItemsLeft }} // Loop Over Items only: true when the loop is done
```

`$json` is NOT available in a Code node running "Run Once for All Items", use `$input.all()` or `$input.first()` there. It IS available when running "Run Once for Each Item".

## Webhook node: who responds, and with what

The Webhook node's **Respond** setting decides timing; **Response Data** decides the body. Both are on the Webhook node itself, not on the workflow.

**Respond = Immediately**, replies as soon as the Webhook node executes. The body is the response code plus the message "Workflow got started". The rest of the workflow keeps running but the caller never sees its result.

**Respond = When Last Node Finishes**, holds the HTTP connection open until the workflow completes, then returns the response code plus data from the last executed node. **Response Data** (visible only for this mode) picks the body shape:

- **All Entries**: all output items of the last node, as an array.
- **First Entry JSON**: JSON of the first entry of the last node, as an object.
- **First Entry Binary**: binary data of the first entry, as a file.
- **No Response Body**: status code only.

**Respond = Using 'Respond to Webhook' Node**, replies when the flow reaches a Respond to Webhook node, using that node's configured status code, body, and headers. Full control, including redirects (status 301/302 plus a `Location` header) and custom error bodies.

Gotchas:

- If the workflow contains a Respond to Webhook node but the Webhook node is NOT set to "Using 'Respond to Webhook' Node", the execution fails with `Unused Respond to Webhook node found in the workflow`. The mode must match the node.
- Conversely, set to "Using 'Respond to Webhook' Node" with no such node in the flow means the caller hangs until it times out. Only one Respond to Webhook node may execute per run.
- Long synchronous mode: "When Last Node Finishes" keeps the caller's connection open for the whole run. Senders with short timeouts will see a timeout even though the workflow succeeded. Use "Immediately" for fire-and-forget, or "Using 'Respond to Webhook' Node" to reply early (for example a quick 202 ack) and keep processing after it.

## Webhook output shape

Items leaving a Webhook trigger node look like this:

```json
{
  "headers": { "content-type": "application/json" },
  "params": {},
  "query": { "campaign": "spring" },
  "body": { "full_name": "Ava", "email_address": "ava" }
}
```

So the posted payload is at `{{ $json.body.full_name }}`, not `{{ $json.full_name }}`. Query string values are at `{{ $json.query.campaign }}`.

## Quick debug checklist

1. `undefined` on a field that clearly exists upstream → you are reading `$json` after a node that replaced the item. Use `$('Node Name').first().json.FIELD`.
2. `Info for expression missing from previous node` → a Code node upstream returned items without `pairedItem`. Add it.
3. `Multiple matching items for expression` → an aggregation or Merge is upstream. Replace `.item` with `.first()`, `.last()`, or `.all()[INDEX]`.
4. Caller gets "Workflow got started" instead of real data → Webhook Respond is set to "Immediately"; switch to "When Last Node Finishes".
5. Caller hangs forever → Webhook expects a Respond to Webhook node that never executes, or the branch containing it did not run.
6. Test an expression safely: drop a Set node after the node in question and read `{{ JSON.stringify($json) }}` there before wiring the expression into the real node.


---

Source: [Vectle](https://vectle.com/skills/skl_t_E-6rEwgmRKW5MD1kRJWw). Version: `skv_JH7fXYl_o2SkMXgLrqT2VQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

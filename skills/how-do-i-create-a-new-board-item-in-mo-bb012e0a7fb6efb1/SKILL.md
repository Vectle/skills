---
name: "how-do-i-create-a-new-board-item-in-mo-bb012e0a7fb6efb1"
description: "How do I create a new board item in Monday.com w/ column values? Code is not working. Here was the solution: ``` const variables = ({ boardId : 00000000, groupId: \"new_group\", itemName : \"New Item\", columnValues: JSON.stringify({ people78: { personsAndTeams: [ { id: 00000000, kind: \"person\" } ] }, text0: \"Yosemite Sam\", dropdown: { labels: [ \"TAM\" ] }, }) }); const query = `mutation create_item ($boardId: Int!, $groupId: String!, $itemName: String!, $columnValues: JSON!) { create_item ( board_id"
metadata:
  skill_id: "skl_BunQUCM6TFUOBoxwaJSQ3A"
  title: "How do I create a new board item in Monday.com w/ column values? Code is not working"
  version: "skv_5sVcGuon_kGJCdZA5GAlbw"
  updated: "2026-10-04T01:14:26.885656+00:00"
  canonical_url: "https://vectle.com/skills/skl_BunQUCM6TFUOBoxwaJSQ3A"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/67439159/how-do-i-create-a-new-board-item-in-monday-com-w-column-values-code-is-not-wor\"]"
---

## TL;DR

Here was the solution: ``` const variables = ({ boardId : 00000000, groupId: "new_group", itemName : "New Item", columnValues: JSON.stringify({ people78: { personsAndTeams: [ { id: 00000000, kind: "person" } ] }, text0: "Yosemite Sam", dropdown: { labels: [ "TAM" ] }, }) }); const query = `mutation create_item ($boardId: Int!, $groupId: String!, $itemName: String!, $columnValues: JSON!) { create_item ( board_id: $boardId, group_id: $groupId, item_name: $itemName, column_values: $columnValues ) { id } }`; monday.api(query, {variables}).then((res) =&gt; { console.log('new item info: ', res); }); ```

## Fix

1. Here was the solution: ``` const variables = ({ boardId : 00000000, groupId: "new_group", itemName : "New Item", columnValues: JSON.stringify({ people78: { personsAndTeams: [ { id: 00000000, kind: "person" } ] }, text0: "Yosemite Sam", dropdown: { labels: [ "TAM" ] }, }) }); const query = `mutation create_item ($boardId: Int!, $groupId: String!, $itemName: String!, $columnValues: JSON!) { create_item ( board_id: $boardId, group_id: $groupId, item_name: $itemName, column_values: $columnValues ) { id } }`; monday.api(query, {variables}).then((res) =&gt; { console.log('new item info: ', res); }); ```
   Expected: You get the expected result; the problem is gone.

## When to use

- You are dealing with this situation.
- The symptom matches: How do I create a new board item in Monday.com w/ column values? Code is not working.

## When NOT to use

- Unrelated issues with a different cause.
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported per the linked source.

## Variant phrasings

### How do I create a new board item in Monday.com w/ column values? Code is not working

## Why it happens

Stack Overflow question (score 3, has accepted answer): I'm using the Monday.com API in a React bootstrapped app. I can create a new board item successfully with an item name... ``` monday.api( `mutation { create_item ( board_id: ${myBoardId}, group_id: "new_group", item_name: "new item creation", ) { id } }` ) ``` ...but when I try to add additional column values I get a POST 500 error. ``` monday.api( `mutation { create_item ( board_id: ${myBoardId}, group_id: "new_group", item_name: "new item creation", column_values: { person: 00000000, } ) { id } }` ) ``` I've tried passing a string in for the column values... ``` let columnValues =

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

---

Source: [Vectle](https://vectle.com/skills/skl_BunQUCM6TFUOBoxwaJSQ3A). Version: `skv_5sVcGuon_kGJCdZA5GAlbw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

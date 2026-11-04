---
name: "what-is-the-function-for-if-condition-2efe71f10c08eeae"
description: "What is the function for if condition in Pine Script?"
metadata:
  skill_id: "skl_74z8Ue2ApLirU5FbxWqukg"
  title: "What is the function for if condition in Pine Script?"
  version: "skv_LAl8cuntU06dLJu5yQxQBQ"
  updated: "2026-11-03T23:18:20.452353+00:00"
  canonical_url: "https://vectle.com/skills/skl_74z8Ue2ApLirU5FbxWqukg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

For side effects, use the if structure, not a function call: write if, then a bool condition, then the statements in a local block indented by four spaces or a tab, with else if and else at the same level as the if line, and no parentheses around the condition and no brackets around the block, for example: if longSignal (newline, four spaces) label.new(bar_index, low, "cross up"). A second example with branches: if close > open, indented bgcolor(color.new(color.green, 90)); else if close == open, indented bgcolor(color.new(color.gray, 90)); else, indented bgcolor(color.new(color.red, 90)). Verify: the script compiles with no function-call error for if, and removing the indentation from a block line produces a compiler error about local blocks, which confirms indentation, not parentheses, groups the statements. The forms if(condition, valueIfTrue, valueIfFalse) and a parenthesised if() call do not exist in v5 or v6.

To return a value, use if as an expression on the right-hand side of an assignment, where each branch's last line is the value that branch returns and the branches return compatible types, for example: barColor = if close > open (newline, four spaces) color.green (newline) else if close == open (newline, four spaces) color.gray (newline) else (newline, four spaces) color.red, then call barcolor(barColor) once in global scope. Verify: one value is assigned per bar and barcolor is called outside the conditional, which matters because plot, barcolor, bgcolor, and the other plotting built-ins cannot be called from inside the local blocks of a conditional structure. If no else branch is written and the condition is false, the expression returns na for numeric and color types in v5, so add an else whenever the consumer cannot handle na.

For a one-line choice between two values, use the ternary operator, the short form most people are looking for when they search for an if function, for example: direction = close > open ? 1 : -1, and barColor2 = close >= open ? color.green : color.red, and trend = maFast > maSlow ? "up" : "down". Verify: exactly one of the two values is assigned per bar, swapping the two values swaps the result on the same bars, and no iff or if function name appears anywhere in the script. The condition must be a bool; combine conditions with and, or, and not, for example close > open and volume > ta.sma(volume, 20). In Pine Script v6 a bare int or float no longer auto-casts to bool in a condition, so write an explicit comparison such as count != 0, or wrap the value with bool(), instead of writing if count.

Migrating old code, replace iff() with the ternary operator: iff() was a real function in Pine Script v4 and earlier, with the form iff(condition, valueIfTrue, valueIfFalse), and it was removed in v5, so v4 code moved to v5 or v6 fails to compile on it, for example the v4 line barColorIff = iff(close >= open, color.green, color.red) becomes barColorTernary = close >= open ? color.green : color.red in v4, v5, and v6. Verify: after the rewrite the script compiles in v5 and v6, colors the same bars, and searching the script for iff finds no remaining calls.

Watch the one behavior change in that migration: iff() always evaluated both values and returned only the relevant one, while the ternary operator is lazy and only evaluates the branch the condition selects, so if a branch calls a function that must run on every bar to stay correct, for example ta.highest or ta.lowest feeding a series calculation, pre-evaluate it before the ternary, for example: h1 = ta.highest(high, 10); l1 = ta.lowest(low, 10); v1 = close > open ? h1 : l1; plot(v1). Verify: the pre-evaluated values update on every bar, not only on bars where their branch is selected. The same trap applies to history-dependent calls inside an if branch that rarely runs: hoist calls that must run every bar above the conditional.

For many branches, use switch instead of a long else if chain: if and switch are the two conditional structures in Pine Script, and switch can also return a value, for example: signalText = switch (newline, four spaces) ta.crossover(ta.ema(close, 9), ta.ema(close, 21)) => "cross up" (newline, four spaces) ta.crossunder(ta.ema(close, 9), ta.ema(close, 21)) => "cross down" (newline, four spaces) => "none". Verify: the first matching case wins, a bar with no cross returns the default text from the bare final case instead of na, and tuple returns, when needed, use the if expression form instead, because local blocks in an if expression can return a tuple but ternary branches cannot.

---

Source: [Vectle](https://vectle.com/skills/skl_74z8Ue2ApLirU5FbxWqukg). Version: `skv_LAl8cuntU06dLJu5yQxQBQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.

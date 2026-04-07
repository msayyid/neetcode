# Longest Repeating Character Replacement - Full Notes

## Core idea

We want the length of the longest substring that can be turned into one repeating character using at most `k` replacements.

For any window, the optimal strategy is:

* keep the most frequent character
* replace all other characters

So the number of replacements needed is:

`window length - max frequency`

If this is `<= k`, the window is valid.
If this is `> k`, the window is invalid.

---

## Why `window length - max frequency` works

Example: `"BABB"`

* length = 4
* most frequent character = `B`
* frequency = 3

So:

`4 - 3 = 1`

We only need 1 replacement:

`BABB → BBBB`

Important understanding:

We always choose the most frequent character because it minimizes replacements.
Choosing any other character would require more replacements.

---

## Sliding window approach (optimized)

We maintain:

* a frequency dictionary (`count`)
* left pointer `l`
* right pointer `r`
* result `res`
* `maxf` = max frequency seen so far

---

## Mental execution template (IMPORTANT)

For each step:

1. Expand → add `s[r]` to the window
2. Update frequency and `maxf`
3. Check if window is valid:

   * `window_len - maxf > k` → invalid
4. If invalid → shrink from left (while loop)
5. Once valid → update `res`

---

## Golden rules

* Always expand first
* Shrink only when invalid
* Stop shrinking immediately when valid
* Only then update `res`

---

## Common mistake you had

You thought:

> we might keep shrinking even after the window becomes valid

Correction:

We stop shrinking as soon as the condition is satisfied.
Then we go back to expanding.

---

## Another important mistake you had

You thought:

> we shrink into the next valid window (like directly going from `"ABAB"` → `"BABB"`)

Correction:

That is wrong.

Actual flow is:

* `"ABAB"` (valid) → expand → `"ABABB"`
* then shrink → `"BABB"`

👉 Expand first, then shrink if needed

---

## Why we decrement count when moving `l`

Because the character at `l` leaves the window.

We must keep the frequency map accurate for the current window.

---

## Why we use `while` and not `if`

Because shrinking once may not be enough.

Example:

* window needs 4 replacements
* `k = 1`

Shrinking once → still invalid
So we must keep shrinking until valid

---

## Understanding `maxf` (VERY IMPORTANT)

### What `maxf` really is

`maxf` = the highest frequency we have **ever seen while expanding**

It is NOT always the exact max in the current window.

It can become **stale (too large)**.

---

## Your confusion about `maxf`

You asked:

> how does this guarantee the correct max each time?

Answer:

It does NOT guarantee the exact current max.

It guarantees:

* `maxf` is an upper bound
* and that is enough

---

## Why stale `maxf` still works

If `maxf` is too big:

* `window_len - maxf` becomes smaller
* so we may treat an invalid window as valid

This seems wrong, but:

👉 it does NOT break the answer

---

## Key intuition (this is the real understanding)

If we reach a window of size `X`, it means:

> at some point, we had enough repeating characters to support that size

So even if the current window is slightly invalid:

* a valid window of that size **already existed or will exist**

We never miss the correct answer.

---

## Example of stale `maxf`

Window becomes `"ABAB"`

* actual max freq = 2
* but `maxf = 3` (stale)

We think:

`4 - 3 = 1` → valid

But actually:

`4 - 2 = 2` → invalid

Still okay because:

* we already had `"AABA"` (valid size 4 earlier)
* so we are not inventing a fake answer

---

## One-line explanation (interview-ready)

We allow `maxf` to be stale because it only makes the window more permissive, and since we only care about the maximum length, it does not affect correctness.

---

## Brute force approach (your understanding)

For each index `i`:

* start a new window
* reset `count` and `maxf`
* expand `j` from `i` to end
* check validity for each substring

This generates all substrings:

* `[i...i], [i...i+1], [i...i+2], ...`

You correctly understood:

* we do NOT shrink
* we just keep expanding `j`

---

## Small correction you needed

You described jumps like:

> A → AAABABB

That is incorrect.

Correct flow is gradual:

* `"A"`
* `"AA"`
* `"AAA"`
* `"AAAB"`
* `"AAABA"`
* ...

---

## Time and space complexity

### Sliding window

* Time: O(n)
* Space: O(1)

### Brute force

* Time: O(n²)
* Space: O(1)

---

## Final mental model

This problem is about:

> growing the window as much as possible, and only shrinking when forced

---

## Short summary

* Use sliding window
* Track frequencies
* Use `window_len - maxf` to check validity
* Shrink only when invalid
* `maxf` can be stale, and that is okay
* Always expand first, shrink if needed, then update result

---

## Your key breakthroughs

You understood:

* why we subtract max frequency
* why shrinking is needed
* why `while` is required
* how sliding window differs from brute force
* and most importantly, how stale `maxf` still works

That last one is what most people struggle with.

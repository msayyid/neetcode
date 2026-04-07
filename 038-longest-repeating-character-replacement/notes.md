# Longest Repeating Character Replacement - Notes

## Core idea

We want the length of the longest substring that can be turned into one repeating character using at most `k` replacements.

For any current window, the cheapest way to make all characters the same is:

* keep the character that appears the most
* replace all the other characters

So the number of replacements needed is:

`window length - max frequency in the window`

If this value is `<= k`, the window is valid.
If this value is `> k`, the window is invalid.

---

## Why `window length - max frequency` works

Example: `"BABB"`

* length = 4
* most frequent character = `B`
* frequency of `B` = 3

So:

`4 - 3 = 1`

That means only 1 replacement is needed to make the whole window one repeating character.

Example:

`BABB -> BBBB`

We always keep the most frequent character because that gives the minimum number of replacements.

If we tried to make the whole window equal to a less frequent character, we would need more replacements.

---

## Sliding window idea

We use a sliding window with:

* a frequency dictionary to count characters in the current window
* `l` as the left pointer
* `r` as the right pointer
* `res` to store the longest valid window found so far

As `r` moves right:

1. add the new character into the frequency map
2. check whether the window is still valid
3. if it is not valid, move `l` right and decrease the count of the character leaving the window
4. once valid, update the answer

---

## What each variable does

`count`
Stores frequencies of characters inside the current window.

`l`
Left boundary of the window.

`r`
Right boundary of the window.

`res`
Best valid window length seen so far.

---

## Why we decrement the left character count

When we shrink the window, the character at `l` is no longer inside the window.

So before moving `l`, we decrease its frequency in the dictionary.

This keeps the frequency map accurate for the current window.

---

## Why we use `while` and not `if`

One shrink may not be enough.

A window can still remain invalid after removing just one character from the left, so we must keep shrinking until it becomes valid again.

Example idea:

* window needs 4 replacements
* but `k = 1`

Shrinking once might make it need 3 replacements, which is still invalid.

So `if` is not enough.
We need `while`.

---

## Important intuition

A valid window means:

`window length - max frequency <= k`

This means:

the number of characters we need to replace is at most `k`.

---

## Example walkthrough

Window = `"ABBBAC"`, `k = 2`

* length = 6
* max frequency = 3 (`B`)
* replacements needed = `6 - 3 = 3`

This is invalid because `3 > 2`.

Shrink from the left.

New window = `"BBBAC"`

* length = 5
* max frequency = 3
* replacements needed = `5 - 3 = 2`

Now it is valid.

That means we can replace `A` and `C` with `B`:

`BBBAC -> BBBBB`

---

## Time complexity

The version you studied is effectively `O(26 * n)`, which becomes `O(n)` for this problem.

Why:

* `r` moves through the string once
* `l` also moves through the string at most once
* finding `max(count.values())` checks at most 26 uppercase letters

So it simplifies to linear time.

---

## Space complexity

`O(26)`, which simplifies to `O(1)` for this problem.

Why:

* the string contains only uppercase English letters
* so the frequency dictionary can have at most 26 keys

---

## Common understanding checks

Why do we subtract the max frequency?
Because we keep the most common character and replace the rest.

Why not choose some other character as the target?
Because that would require more replacements, not fewer.

Why do we shrink the window?
Because if the replacements needed are more than `k`, the window does not satisfy the requirement.

Why do we update `res` only after shrinking?
Because only then the window is guaranteed to be valid.

---

## Short summary

This is a sliding window problem.

For each window:

* count character frequencies
* find the most frequent character
* calculate how many replacements are needed
* if too many replacements are needed, shrink the window
* keep track of the longest valid window
**Merge Strings Alternately — LeetCode Easy**

**What the problem asks:**
Take one char from word1, one from word2, alternating. If one string is longer, append the rest at the end.

**My approach:**
Loop `len(word1) + len(word2)` times. At each iteration `i`, check if `i < len(word1)` and append, then check if `i < len(word2)` and append. Two separate `if` statements (not `if/else`) so both can fire in the same iteration.

**Mistakes I made:**
- Originally used `word1[i]` and `word2[i]` directly with the loop variable `i`, which would cause an index out of bounds error when `i` exceeds the length of either string. Fixed by guarding with `if i < len(word1)` and `if i < len(word2)`.
- Had redundant `count` and `count1` variables that were always equal to `i` — removed them entirely.

**Why it works for unequal lengths:**
When one string is exhausted, its `if` check fails silently and we just keep appending from the longer string. No special casing needed.

**Time complexity:** O(n) where n is the total number of characters in both strings. The loop is O(n) and `"".join()` is also O(n).

**Space complexity:** O(n) — storing the result in a list. This is optimal; you cannot avoid storing the output.
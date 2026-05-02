**Valid Palindrome II — Notes**

**Approach:** Two pointers (`l`, `r`) moving inward. Helper function `is_palindrome(s, l, r)` checks a substring with no deletions allowed.

**Key insight:** When a mismatch is found, you have exactly **one deletion** to use — either skip the left character or the right. You can't peek ahead to decide which is correct, so you **try both** and return `True` if either substring is a valid palindrome. The very first mismatch is the only place we can make a cut — whatever we decide there determines everything.

**In my own words:**
We have `l` and `r` pointers referring to the start and end of `s`. We loop while they haven't met. If they don't match, we try two cuts — skip left (`l+1, r`) and skip right (`l, r-1`) — and send each to the helper which checks if that substring is a palindrome using the same two pointer approach but with no deletions allowed. If either returns `True`, we return `True`. If both return `False`, it means we'd need more than one deletion, so we return `False`.

**Traces:**
- `"aca"` — we never enter the if, `l` and `r` just meet, return `True`
- `"abbadc"` — first iteration hits mismatch, `"bbadc"` is not a palindrome, `"abbad"` is not a palindrome, both `False` → return `False`
- `"abbda"` — first iteration `'a'=='a'` passes, second iteration `l=1, r=3`, `'b'!='d'`, skip left gives `"bd"` → `False`, skip right gives `"bb"` → `True`, `False or True` → return `True`

**Mistakes I made:**
- Tried to handle the skip inline with modified pointer jumps (`r -= 2`, `l += 2`) — these don't represent skipping one character, they jump too far
- Tried peeking ahead (`s[l+1] != s[r]`) to decide which to skip upfront — this doesn't always work, you have to try both
- `s[::-1]` reverses the whole string, not the substring — needed `s[l:r+1][::-1]`
- `s[r+1:l-1:-1]` breaks when `l=0` because `-1` in slices means last character in Python

**What I learned:**
- When inline logic gets complicated, extract a helper function
- Two versions of the helper:
    - **O(n) space** — slicing: `return s[l:r+1] == s[l:r+1][::-1]` — clean and readable but creates new strings in memory
    - **O(1) space** — two pointers inside the helper, no new strings created, more interview-friendly
- `s[l:r+1][::-1]` reverses a substring slice cleanly

**Complexities:**
- Time: O(n) — main loop + helper called at most once
- Space: O(n) with slicing version, O(1) with two-pointer version

**Valid Palindrome II — Notes**

**Approach:** Two pointers (`l`, `r`) moving inward. Helper function `is_palindrome(s, l, r)` checks a substring with no deletions allowed.

**Key insight:** When a mismatch is found, you have exactly **one deletion** to use — either skip the left character or the right. You can't peek ahead to decide which is correct, so you **try both** and return `True` if either substring is a valid palindrome.

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

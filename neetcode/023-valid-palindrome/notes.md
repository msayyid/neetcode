**Valid Palindrome — Session Notes**

**Problem:** Given a string, return true if it reads the same forwards and backwards, ignoring case and non-alphanumeric characters.

---

**Solution 1 — Filter + Reverse (Brute Force)**
```python
s_array = []
for c in s:
    if c.isalnum():
        s_array.append(c.lower())
return s_array == s_array[::-1]
```

**What I did:** Filter the string into a list keeping only alphanumeric characters, lowercased. Then check if the list equals its reverse using `[::-1]`.

**Mistakes I made:**
- Initially used a manual set `alph_nums` with all letters/digits — unnecessary since `.isalnum()` does exactly this in O(1)
- Had a duplicate `'0'` in the set — sets deduplicate silently, not a bug but sloppy
- Used string concatenation `s += char` in a loop — this is **O(n²)** because strings are immutable in Python, each concatenation creates a new string. Fixed by appending to a list (O(1) amortised) and joining once
- Forgot `.lower()` when appending, which broke case-insensitive comparison
- Used `for i in range(len(s))` — not Pythonic, prefer `for c in s`

**Things I learned:**
- String concatenation in a loop is O(n²) — always use a list and join
- `.isalnum()` is a built-in that replaces manual character range checks, O(1) on a single char
- Set lookup is O(1), string lookup is O(n)
- List comparison works fine — no need to convert back to string
- `list[::-1]` reverses a list in one clean expression

**Complexity:** Time O(n), Space O(n)

---

**Solution 2 — Two Pointers (Optimal)**
```python
l, r = 0, len(s) - 1
while l < r:
    if s[l].isalnum() and s[r].isalnum():
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    elif not s[l].isalnum():
        l += 1
    elif not s[r].isalnum():
        r -= 1
return True
```

**What I did:** Two pointers starting from each end. Skip non-alphanumeric characters by moving the respective pointer. When both point to valid characters, compare them case-insensitively. If mismatch, return False. If pointers cross, return True.

**Mistakes I made:**
- Initially used raw ASCII ranges (`48 <= ord(c) <= 57` etc.) — verbose and error-prone, `.isalnum()` replaces all of it
- Forgot to move `l` and `r` after a successful match — caused infinite loop
- Forgot `.lower()` on comparison — broke case-insensitive check

**Things I learned:**
- Two pointer pattern: work from both ends, move pointers based on conditions
- Skip invalid characters independently on each side before comparing
- `.isalnum()` and `.lower()` are your friends — use them freely in interviews

**Complexity:** Time O(n), Space O(1) — no extra memory, just two pointers

---

**Key Takeaway:** Solution 2 is optimal for interviews. Solution 1 is more readable and acceptable, but uses O(n) space. Know both and know why.

---
### Solution 3

1. The inner `while` loops to skip non-alphanumeric characters is actually **neater** than your previous if/elif chain — it handles the skipping in one go before the comparison
2. Using `ord("A")` instead of hardcoded `65` is more readable — good practice
3. `l, r = l + 1, r - 1` is a nice Pythonic simultaneous assignment

The only thing worth noting for interviews — you're implementing `.isalnum()` manually here. That's absolutely fine and actually **shows you understand ASCII**, but be ready to explain why you chose this over the built-in if asked.



**Solution 3 — Two Pointers with ASCII helper (same complexity as Solution 2)**

```python
def alpha_num(self, c):
    return (ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9"))
```

**What's different:** Uses inner `while` loops to skip non-alphanumeric characters on each side before comparing — cleaner than if/elif chain. Implements alphanumeric check manually via ASCII ranges instead of `.isalnum()`, demonstrating understanding of how character encoding works.

**Complexity:** Time O(n), Space O(1)
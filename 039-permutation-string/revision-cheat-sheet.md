# 🧩 Permutation in String - Quick Revision

## Problem

Check if any permutation of `s1` exists as a substring in `s2`.

👉 Equivalent to:

> Does any substring of length `k = len(s1)` in `s2` have the **same character count** as `s1`?

---

# 🔴 Approach 1 - Brute Force

## Idea

* Loop over all substrings of size `k`
* Build count for each substring
* Compare with `s1` count

---

## Code Template

```python
k = len(s1)

for i in range(len(s2) - k + 1):
    substring = s2[i:i+k]
    if count(substring) == count(s1):
        return True
return False
```

---

## Complexity

* Time: **O(n * k)**
* Space: **O(1)**

---

## Key weakness

❌ Rebuilds count every time

---

# 🟢 Approach 2 - Sliding Window (Optimal)

## Idea

* Build count for `s1`
* Build count for first window in `s2`
* Slide window:

  * add new char
  * remove old char
* compare counts

---

## Code Template

```python
k = len(s1)

# build count1
# build count2 for first window

if count1 == count2:
    return True

for r in range(k, len(s2)):
    add s2[r]
    remove s2[r - k]

    if count1 == count2:
        return True

return False
```

---

# 🔥 Main Loop (MOST IMPORTANT)

At every step:

```text
Add → s2[r]
Remove → s2[r - k]
```

---

## Why `r - k`?

* Window size = k
* Right pointer = r
* Leftmost element = `r - k`

---

## Example

```text
s2 = "abcdef", k = 3

r = 3 → add 'd', remove 'a'
r = 4 → add 'e', remove 'b'
r = 5 → add 'f', remove 'c'
```

---

# ⚡ Complexity

## Time

* Brute force: **O(n * k)**
* Optimal: **O(n)**

## Space

* Both: **O(1)** (26 letters)

---

# 🧠 Key Insight

### Brute force:

```
recompute whole window ❌
```

### Optimal:

```
update only 2 chars ✅
```

---

# 🎯 Interview Answer

> I use a sliding window of size `len(s1)`.
> Instead of recomputing frequency each time, I update it by adding the new character and removing the old one, reducing complexity to O(n).

---

# 🚨 Common Mistakes

* ❌ Using `s2[i:i+k]` in optimal solution
* ❌ Wrong loop bounds → index out of range
* ❌ Forgetting to check first window
* ❌ Using `i` instead of `r`

---

# 🧩 Mental Model

Always think:

```text
Window moves → only 2 changes
```



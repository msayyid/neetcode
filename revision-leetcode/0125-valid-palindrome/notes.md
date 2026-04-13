# 🧠 125. Valid Palindrome - Notes

## 🔹 Problem Summary

Check if a string is a palindrome after:

* converting to lowercase
* removing all non-alphanumeric characters

---

## 🔹 Core Idea (Two Pointers)

* Use two pointers:

  * `l` → start
  * `r` → end
* Move inward while:

  * skipping invalid characters
  * comparing valid ones

---

## 🔹 Key Insight

👉 Only compare **alphanumeric characters**

👉 Ignore:

* spaces
* punctuation
* symbols

---

## 🔹 Algorithm (Mental Model)

```text
while l < r:

    if left is invalid:
        move l
        continue

    if right is invalid:
        move r
        continue

    if mismatch:
        return False

    move both pointers

return True
```

---

## 🔹 Final Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
```

---

## 🔹 Why `continue` is important

* Skips rest of loop immediately
* Prevents comparing invalid characters
* Ensures:

  > “compare only when both sides are clean”

---

## 🔹 Complexity

* Time: **O(n)**
* Space: **O(1)**

---

## 🔹 Edge Cases

* `" "` → True
* `"!!!"` → True
* `"a."` → True
* `"race a car"` → False

---

## 🔹 Common Mistakes

❌ Using `.isalpha()` instead of `.isalnum()`
❌ Forgetting `.lower()`
❌ Moving `r` in wrong direction (`r += 1`)
❌ Not skipping invalid characters → infinite loop

---

## 🔹 Alternative Approach (Less Optimal)

```python
filtered = ''.join(c.lower() for c in s if c.isalnum())
return filtered == filtered[::-1]
```

* Easier
* But uses **O(n) space**

---

## 🔹 How to Explain in Interview

You can say:

> I use two pointers from both ends.
> I skip non-alphanumeric characters and compare lowercase versions.
> If there's a mismatch, I return False. Otherwise, I keep shrinking the window.
> This gives O(n) time and O(1) space.

---

## 🔹 Pattern Recognition

This is a classic:

* **Two pointers**
* **String cleaning on the fly**

---

## 🔹 Follow-up Problem

👉 “Valid Palindrome II” (allow 1 deletion)
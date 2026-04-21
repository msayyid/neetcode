# 🧾 Remove All Adjacent Duplicates in String - Notes

## 🔹 Core Idea

We repeatedly remove **adjacent duplicates** until no more can be removed.

Instead of actually removing from the string multiple times (inefficient), we:

> Use a **stack** to simulate the process in one pass.

---

## 🔹 Key Logic

* Traverse the string character by character
* For each character:

  * If it is the same as the top of the stack → **pop (remove pair)**
  * Else → **push (keep character)**

---

## 🔁 Why Stack Works

Stack always represents:

> “the current valid string after all removals so far”

So:

* Push = keep character
* Pop = remove adjacent duplicate

---

## 🧠 Example Walkthrough

```
s = "abbaca"

stack = []

a → push → [a]
b → push → [a, b]
b → same as top → pop → [a]
a → same as top → pop → []
c → push → [c]
a → push → [c, a]

result = "ca"
```

---

## ⏱️ Time Complexity

* Traverse string → O(n)
* Join stack → O(n)

Final:

> **O(n)**

---

## 📦 Space Complexity

* Stack can hold up to n characters

> **O(n)**

---

## ❌ Mistakes I Made

### 1. Thought space is O(1)

* Assumed only 26 letters → O(26)
* ❌ Wrong because:

  * Stack stores **occurrences**, not unique characters
  * Example: `"abababab"` → stack size = n

---

### 2. Forgot stack represents full state

* Initially thought it only stores “important” chars
* Actually:

  > It stores the entire remaining valid string

---

### 3. Used index-based loop unnecessarily

* Started with:

  ```python
  stack = [s[0]]
  for i in range(1, len(s)):
  ```
* Better:

  ```python
  for c in s:
  ```
* Cleaner and safer

---

## ✅ Things I Learned

* Stack is perfect for:

  > “remove adjacent / matching / canceling elements”

* Always think:

  > “Can I simulate the process instead of actually modifying the string?”

* Space complexity:

  > Based on number of elements stored, not number of unique values

---

## 🧩 Pattern Recognition

This is a **classic pattern**:

> “Use stack when elements cancel each other”

Similar problems:

* Valid Parentheses
* Backspace String Compare
* Removing duplicates / simplifying sequences

---

## 🎯 Key Takeaway (Important)

> “Even with limited character set, stack can grow to size n because removals depend on adjacency, not frequency.”

---

## 🧼 Final Clean Code

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
```
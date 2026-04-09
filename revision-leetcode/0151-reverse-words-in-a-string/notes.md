# 🧾 Reverse Words in a String - Full Notes

---

# 🧠 Problem Summary

Given a string:

* Words are separated by spaces
* May contain:

  * leading spaces
  * trailing spaces
  * multiple spaces between words

👉 Goal:

* Reverse word order
* Return string with **single spaces only**

---

# 🔴 Approach 1 - String Concatenation (BAD)

## Code

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""

        for i in range(len(s)):
            if s[i] != " ":
                word += s[i]   # ❌ PROBLEM
            else:
                if word:
                    words.append(word)
                    word = ""

        if word:
            words.append(word)

        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)
```

---

## ❗ Mistake you made

You assumed:

```python
word += s[i]
```

is O(1)

---

## 🔥 Reality

Each time:

* new string is created
* old string is copied

Example:

```
"a" → copy 1
"ab" → copy 2
"abc" → copy 3
```

👉 Total = 1 + 2 + 3 + ... = **O(n²)**

---

## ⏱ Complexity

* Time: **O(n²)** ❌
* Space: **O(n)**

---

## ❌ Verdict

* Works
* **Not interview safe**

---

# 🟠 Approach 2 - List + Join (Improved)

## Code

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = []

        for i in range(len(s)):
            if s[i] != " ":
                word.append(s[i])   # ✅ O(1)
            else:
                if word:
                    words.append("".join(word))
                    word = []

        if word:
            words.append("".join(word))

        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)
```

---

## 🧠 Key improvement

* Use list instead of string
* `append()` is O(1)
* `join()` copies once

---

## ⏱ Complexity

* Time: **O(n)**
* Space: **O(n)**

---

## ⚠️ Still not optimal

* Stores words separately
* Extra structure

---

# 🟡 Approach 3 - Cleaner parsing (your improved version)

## Code

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word_chars = []

        for ch in s:
            if ch != " ":
                word_chars.append(ch)
            else:
                if word_chars:
                    words.append("".join(word_chars))
                    word_chars = []

        if word_chars:
            words.append("".join(word_chars))

        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)
```

---

## 🧠 What you improved

* Iterating directly (`for ch in s`)
* Correct condition:

```python
if word_chars:
```

---

## ⏱ Complexity

* Time: **O(n)**
* Space: **O(n)**

---

## ⚠️ Still not optimal

* Uses extra `words[]`

---

# 🟢 Approach 4 - Python Built-in (Simple)

## Code

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        m = s.split()
        m.reverse()
        return " ".join(m)
```

---

## 🧠 What you didn’t know (IMPORTANT)

### `split()` does ALL of this:

```python
s = "  hello   world  "
```

👉 becomes:

```python
["hello", "world"]
```

✔ removes leading spaces
✔ removes trailing spaces
✔ compresses multiple spaces

---

## ⏱ Complexity

* Time: **O(n)**
* Space: **O(n)**

---

## ✅ When to use

* First answer in interview

---

# 🟢 Approach 5 - Optimal (Two Pointers)

👉 **Your best solution**

---

## Code

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        array = list(s)
        array.reverse()

        i = 0
        while i < len(array):
            if array[i] != " ":
                start = i
                while i < len(array) and array[i] != " ":
                    i += 1
                end = i - 1

                l, r = start, end
                while l < r:
                    array[l], array[r] = array[r], array[l]
                    l += 1
                    r -= 1
            else:
                i += 1

        write = 0
        read = 0

        while read < len(array):
            while read < len(array) and array[read] == " ":
                read += 1

            while read < len(array) and array[read] != " ":
                array[write] = array[read]
                write += 1
                read += 1

            while read < len(array) and array[read] == " ":
                read += 1

            if read < len(array):
                array[write] = " "
                write += 1

        return "".join(array[:write])
```

---

## 🧠 Core idea

### Step 1 - Reverse whole string

```
"the sky"
→ "yks eht"
```

---

### Step 2 - Reverse each word

```
"yks eht"
→ "sky the"
```

---

### Step 3 - Clean spaces

* remove leading spaces
* remove trailing spaces
* keep single spaces

---

## 🧠 Key technique

### Read / Write pointers

* `read` → scans input
* `write` → builds output in-place

---

## ⏱ Complexity

* Time: **O(n)**
* Space:

  * Python: **O(n)**
  * Conceptually: **O(1)**

---

# ❌ Mistakes you made (IMPORTANT)

---

### 1. String concat

```python
word += s[i]
```

👉 O(n²)

---

### 2. Wrong condition

```python
i == " "
```

👉 should be:

```python
array[i] == " "
```

---

### 3. Using `for` instead of `while`

👉 you needed pointer control

---

### 4. Wrong variable check

```python
if word:
```

👉 should be:

```python
if word_chars:
```

---

### 5. Not skipping leading spaces

👉 caused wrong output

---

### 6. Thinking `join()` is O(n²)

👉 it is **O(n)**

---

# ⚖️ Final Comparison

| Approach     | Time  | Space | Interview |
| ------------ | ----- | ----- | --------- |
| `+=` string  | O(n²) | O(n)  | ❌         |
| list + join  | O(n)  | O(n)  | ⚠️        |
| split()      | O(n)  | O(n)  | ✅         |
| two pointers | O(n)  | O(n)* | ⭐ BEST    |

---

# 🎯 How to explain in interview

---

## Step 1

> We can split the string into words, reverse them, and join.

---

## Step 2

> This uses extra space, so we can optimize.

---

## Step 3

> We reverse the whole string, then reverse each word, then clean spaces using two pointers.

---

# 🔥 Final takeaway

* **Practical** → split + join
* **Interview best** → two pointers

---

# 🧠 Key pattern to remember

👉
**Reverse whole → Reverse parts → Clean**

This appears in many problems.
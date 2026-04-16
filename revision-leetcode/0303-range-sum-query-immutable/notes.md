# 📘 Range Sum Query - Immutable (Prefix Sum)

---

# 🧠 Problem Idea

You are given an array `nums` and multiple queries:

```text
sum(left, right) → nums[left] + ... + nums[right]
```

Goal:

* Handle many queries efficiently

---

# ❌ Brute Force

For each query:

```python
sum(nums[left:right+1])
```

* Time per query: `O(n)`
* Total: `O(n * q)` → too slow

---

# ✅ Prefix Sum Idea

Precompute cumulative sums so each query becomes `O(1)`.

---

# 🔑 Core Concept

> Store cumulative sums so we can subtract unwanted parts.

---

# ⚡ Approach 1 (RECOMMENDED) - Prefix with extra 0

---

## 🔧 Build

```python
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]
```

---

## 📌 Meaning

```text
prefix[i] = sum of nums[0 ... i-1]
```

| i   | prefix[i]       | meaning              |
| --- | --------------- | -------------------- |
| 0   | 0               | nothing before start |
| 1   | nums[0]         | first element        |
| 2   | nums[0]+nums[1] | first two            |
| ... | ...             | ...                  |

---

## 🔍 Query

```python
sum(left, right) = prefix[right + 1] - prefix[left]
```

---

## 💡 Why it works

```text
prefix[right + 1] = sum of nums[0 ... right]
prefix[left]      = sum of nums[0 ... left-1]
```

Subtract:

```text
→ nums[left ... right]
```

---

## ✅ Advantages

* No edge cases
* One clean formula
* Interview standard

---

# ⚡ Approach 2 - Prefix without extra 0

---

## 🔧 Build

```python
prefix = [0] * n
prefix[0] = nums[0]

for i in range(1, n):
    prefix[i] = prefix[i - 1] + nums[i]
```

---

## 📌 Meaning

```text
prefix[i] = sum of nums[0 ... i]
```

---

## 🔍 Query

```python
if left == 0:
    return prefix[right]
else:
    return prefix[right] - prefix[left - 1]
```

---

## ⚠️ Drawback

* Must handle `left == 0`
* Easier to make mistakes

---

# 🚨 Mistakes You Made (Important)

---

## ❌ Mistake 1: Forgetting `self.`

```python
prefix = [...]
```

Problem:

* Local variable
* Not accessible in other methods

✔ Fix:

```python
self.prefix = [...]
```

---

## ❌ Mistake 2: Mixing definitions

You confused:

```text
prefix[i] = sum up to i
```

vs

```text
prefix[i] = sum before i
```

👉 These require **different formulas**

---

## ❌ Mistake 3: Using `prefix[right]` instead of `right + 1`

```python
prefix[right] - prefix[left]
```

Problem:

* Misses `nums[right]`

✔ Fix:

```python
prefix[right + 1] - prefix[left]
```

---

## ❌ Mistake 4: Wrong prefix construction

You wrote:

```python
prefix[i] = prefix[i] + nums[i]
```

Problem:

* No accumulation
* Just copying values

✔ Fix:

```python
prefix[i] = prefix[i - 1] + nums[i]
```

---

## ❌ Mistake 5: Wrong subtraction (missing left element)

```python
prefix[right] - prefix[left]
```

Problem:

* Removes too much

Correct:

```python
prefix[right] - prefix[left - 1]
```

---

## ❌ Mistake 6: Not handling `left = 0`

Without extra `0`:

```python
prefix[left - 1]
```

Problem:

* Becomes `prefix[-1]` → wrong

✔ Fix:

```python
if left == 0:
    return prefix[right]
```

---

# 🧠 Key Intuition (MOST IMPORTANT)

---

## Think of prefix as:

### Version 1 (recommended)

```text
prefix[i] = sum BEFORE index i
```

So:

```text
sum(left, right) =
(sum before right+1) - (sum before left)
```

---

## 🔥 Golden Rule

> To include `nums[right]`, you MUST use `right + 1`

---

# ⚡ Complexity

| Step  | Time |
| ----- | ---- |
| Build | O(n) |
| Query | O(1) |
| Space | O(n) |

---

# 🧾 Final Interview Answer

Use:

```python
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]

return prefix[right + 1] - prefix[left]
```

---

# 🧠 Final Takeaway

> Prefix sum turns repeated range sum queries from O(n) → O(1) by precomputing cumulative sums.
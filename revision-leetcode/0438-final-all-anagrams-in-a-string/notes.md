# 🧩 Problem: Find All Anagrams in a String

### Goal

Find all start indices of substrings in `s` that are anagrams of `p`.

---

# ✅ Approach 1: Sliding Window + Frequency Array Comparison

## 💡 Idea

* Use two arrays of size 26:

  * `count1` → frequency of `p`
  * `count2` → frequency of current window in `s`
* Slide a window of size `k = len(p)` over `s`
* Compare arrays at each step

---

## 🔁 Steps

### 1. Edge case

```python
if len(p) > len(s):
    return []
```

---

### 2. Build initial window

* Fill `count1` from `p`
* Fill `count2` from first `k` chars of `s`

---

### 3. Compare first window

```python
if count1 == count2:
    result.append(0)
```

---

### 4. Slide window

For each `r` from `k → len(s)-1`:

* Add new char: `s[r]`
* Remove old char: `s[r - k]`

```python
count2[add] += 1
count2[remove] -= 1
```

* Compare:

```python
if count1 == count2:
    result.append(start_index)
```

---

## ⏱ Complexity

* Time: **O(n)**

  * Comparison is O(26) = O(1)
* Space: **O(1)**

---

## ❗ Common mistakes

* Forgetting edge case
* Wrong index when appending (`r - k + 1`)
* Recomputing counts instead of sliding

---

## 🧠 Key insight

> Instead of recomputing counts, we update only 2 characters per step.

---

# 🚀 Approach 2: Sliding Window + Matches Optimization

## 💡 Idea

Avoid comparing full arrays every time.

* Track `matches` = number of indices where:

```python
count1[i] == count2[i]
```

* If `matches == 26` → valid anagram

---

## 🔁 Steps

### 1. Setup

* Same as before: build `count1`, `count2`

---

### 2. Initialize matches

```python
matches = 0
for i in range(26):
    if count1[i] == count2[i]:
        matches += 1
```

---

### 3. Slide window

For each step:

### ✅ Before updating window

```python
if matches == 26:
    result.append(l)
```

---

### ➕ Add new char (right pointer)

```python
count2[index] += 1
```

Then:

* If now equal → `matches += 1`
* If was equal before → `matches -= 1`

```python
if count2[index] == count1[index]:
    matches += 1
elif count2[index] - 1 == count1[index]:
    matches -= 1
```

---

### ➖ Remove old char (left pointer)

```python
count2[index] -= 1
```

Then:

* If now equal → `matches += 1`
* If was equal before → `matches -= 1`

```python
if count2[index] == count1[index]:
    matches += 1
elif count2[index] + 1 == count1[index]:
    matches -= 1
```

---

### Move window

```python
l += 1
```

---

### Final check

```python
if matches == 26:
    result.append(l)
```

---

## ⏱ Complexity

* Time: **O(n)** (no full comparisons)
* Space: **O(1)**

---

## ❗ Common mistakes (IMPORTANT)

### 1. Wrong match updates

* Forgetting to check **previous state**
* Mixing up `+1` and `-1` logic

---

### 2. Order matters

* Check `matches == 26` **before updating window**

---

### 3. Forgetting final window check

---

## 🧠 Key insight

> Only 2 characters change per step → only they can affect matches

---

# ⚖️ Comparison

| Approach      | Simplicity | Speed           | Interview Use      |
| ------------- | ---------- | --------------- | ------------------ |
| Array compare | Easier     | Slightly slower | ✅ Most common      |
| Matches       | Harder     | Faster          | ⭐ Strong candidate |

---

# 🔥 Final takeaway

* Start with **array comparison** → safe and clear
* If pushed → move to **matches optimization**
* Always explain:

  * why O(n)
  * why 26 → constant
  * how sliding window avoids recomputation

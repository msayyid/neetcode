# 169. Majority Element - Notes

---

# 1. Hashmap (Counting)

### Idea

Count frequency of each element and return the one that appears more than `n // 2`.

---

### Steps

1. Traverse array
2. Store counts in hashmap
3. Traverse hashmap
4. Return element with count > n // 2

---

### Key Insight

* Majority element appears **strictly more than half**
* So only one element can satisfy this

---

### Complexity

* Time: O(n)
* Space: O(n)

---

### Mistakes / Important Notes

```python
# WRONG (your version)
val > (len(nums) / 2)

# CORRECT
val > len(nums) // 2
```

Reason:

* `/` gives float → unnecessary
* `//` keeps integer comparison clean

---

### When to use

* When space is not constrained
* When you want a simple, safe solution

---

---

# 2. Boyer-Moore (Your Version - “User-friendly”)

---

### Idea

Simulate “voting”:

* Same element → +1 vote
* Different element → -1 vote
* When votes cancel → pick new candidate

---

### Key Insight

> Majority element (> n/2) cannot be fully cancelled

---

### Steps

1. Start with first element as candidate
2. Traverse array
3. If same → increment
4. If different → decrement
5. If count == 0 → reset candidate

---

### Mental Model

Think of it like:

* pairs of different elements cancel each other
* majority element survives because it appears more

---

### Complexity

* Time: O(n)
* Space: O(1)

---

### Important Comments (refined)

```python
# previous candidate got fully cancelled by other elements
# so we pick a new candidate
```

```python
# start with 1 because current element is first vote for new candidate
```

---

### Subtle Behavior

```python
if count == 0:
    candidate = nums[i]
    count = 1
```

* Reset happens **after cancellation**
* Current element becomes new candidate immediately

---

### Mistakes to avoid

```python
# forgetting to reset count to 1
```

```python
# thinking we need two pointers (we don’t)
```

---

---

# 3. Boyer-Moore (Canonical Version)

---

### Idea

Same algorithm, cleaner structure:

* Only pick candidate when `count == 0`

---

### Steps

1. Initialize:

   * candidate = None
   * count = 0
2. Traverse:

   * if count == 0 → pick new candidate
   * same → +1
   * different → -1

---

### Core Invariant (VERY IMPORTANT)

```python
# count = net votes for current candidate
```

---

### Key Insight

```python
# same element -> supports candidate (+1)
# different element -> cancels one vote (-1)
```

---

### Critical Rule (your earlier mistake)

```python
# each element must contribute exactly ONCE per iteration (+1 or -1)
```

If you do:

* reset count
* AND increment again in same iteration

→ you **double count → WRONG**

---

### Why reset doesn’t increase count immediately

```python
if count == 0:
    candidate = num
```

Then:

```python
if num == candidate:
    count += 1
```

This ensures:

* each element contributes only once

---

### Complexity

* Time: O(n)
* Space: O(1)

---

---

# Comparison Summary

| Approach      | Time | Space | Difficulty | Notes                |
| ------------- | ---- | ----- | ---------- | -------------------- |
| Hashmap       | O(n) | O(n)  | Easy       | Simple, intuitive    |
| Boyer (yours) | O(n) | O(1)  | Medium     | More intuitive start |
| Boyer (canon) | O(n) | O(1)  | Medium     | Cleanest invariant   |

---

---

# Final Key Takeaways

```python
# Majority element appears more than n/2 times
```

```python
# cancellation idea: different elements eliminate each other
```

```python
# majority element always survives cancellation
```

```python
# count represents net votes, not actual frequency
```


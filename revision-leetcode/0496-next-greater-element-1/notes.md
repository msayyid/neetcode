# 🧠 Problem: Next Greater Element I

---

# ✅ 1. Brute Force Approach (Forward Scan)

### Idea

* For each number in `nums1`:

  1. Find it in `nums2`
  2. Scan to the right
  3. Return first greater element

---

### Key Insight

> “Find position → scan right → first greater”

---

### Time Complexity

* O(n * m)

---

### Why it works

* Directly follows problem definition

---

### Pros

* Very intuitive
* Easy to explain

---

### Cons

* Not optimal
* Repeats work

---

# ✅ 2. Reverse Brute Force (Harder variant)

### Idea

* Scan `nums2` from **right → left**
* Keep a `cur_max` (candidate)
* Stop when you reach `num`

---

### Key Insight

> “Closer elements overwrite farther ones”

---

### What clicked for you

* We compare with `num`, not `cur_max`
* Reverse traversal ensures:

  * only right-side elements are considered
  * closer elements overwrite earlier ones

---

### Mistake / Confusion you had

* Thought:

  > “What if we are checking elements before num?”

✔ Fixed:

* Loop stops at `num`, so we **never touch left side**

---

### Another confusion

> “Why does 5 overwrite 6?”

✔ Answer:

* We care about **closest greater**, not largest

---

### Verdict

* Works, but:

  * harder to understand
  * not commonly used in interviews

---

# 🚀 3. Optimal Approach (Monotonic Stack)

---

## Core Idea

> “Numbers wait in a stack. A bigger number comes and resolves them.”

---

## Algorithm (mental version)

1. Loop through `nums2`
2. Stack stores **waiting numbers**
3. If current number is bigger:

   * pop smaller ones
   * assign their answer
4. Push current number
5. Remaining elements → `-1`
6. Build result from map

---

## Pseudocode

```text
for each n in nums2:
    while stack not empty and n > stack.top:
        prev = stack.pop()
        map[prev] = n
    push n

for remaining in stack:
    map[value] = -1

for x in nums1:
    result.append(map[x])
```

---

## Key Insight

> “Each element is resolved exactly once”

---

## Stack Meaning

* Stack = elements **waiting for next greater**
* Stack is **monotonically decreasing**

---

## Why `while`, not `if`

Because:

```text
5 resolves 3, 2, 1 → not just one element
```

---

# ❗ Mistakes You Made (Important)

### 1. Missing `-1` handling

* Forgot leftover stack elements

✔ Fix:

```python
while stack:
    map[stack.pop()] = -1
```

---

### 2. Typo bug

```python
nums2[2] ❌
nums2[i] ✔
```

---

### 3. Missing stack initialization

```python
stack = []
```

---

### 4. Overthinking `while` loop complexity

You thought:

> “nested loop → O(n²)?”

✔ Correct understanding:

* each element pushed once
* each element popped once

👉 total = **O(n)**

---

# ⏱️ Complexity

### Time

* O(n + m)

Explanation:

> Each element is pushed and popped at most once

---

### Space

* O(n + m)

  * stack → O(n)
  * hashmap → O(n)
  * result → O(m)

---

# 🔑 Pattern Recognition (VERY IMPORTANT)

You should think **monotonic stack** when you see:

---

## Keywords

* “next greater”
* “next smaller”
* “first greater to the right”
* “nearest greater”
* “daily temperatures”
* “stock span”
* “histogram”

---

## Pattern Trigger

If problem says:

> “for each element, find something to the left/right efficiently”

👉 Think:

```text
monotonic stack
```

---

## Direction matters

| Problem            | Direction    |
| ------------------ | ------------ |
| next greater right | left → right |
| next greater left  | right → left |

---

# 🧠 Mental Model (FINAL)

> “Stack stores waiting elements.
> A bigger number comes and clears smaller ones.”

---

# ⚖️ When to Use Which

| Approach    | Use when             |
| ----------- | -------------------- |
| brute force | simple / small input |
| stack       | optimal / interview  |

---

# 🔥 Final Takeaway

* Brute force = understand problem
* Stack = **solve efficiently**
* Key idea:

```text
each element is handled once → linear time
```

# 🧠 Problem: RecentCounter (Sliding Window - Queue)

---

## 🔹 Core Idea

We are given a stream of timestamps `t` (strictly increasing).

For each `ping(t)`:

> Count how many requests happened in the last 3000 ms → **range [t - 3000, t]**

---

## 🔹 Key Insight

We do NOT recompute from scratch.

Instead:

> Maintain a list of **only valid timestamps**

---

## 🔹 Pattern

### ✅ Sliding Window on Stream + Queue

Triggers:

* “last X time”
* “range [t - k, t]”
* incoming stream (one by one)

👉 Use:

* **Queue (deque)**

---

## 🔹 Approach

For each `ping(t)`:

1. Add current timestamp:

```python
queue.append(t)
```

2. Remove outdated timestamps:

```python
while queue[0] < t - 3000:
    queue.popleft()
```

3. Return count:

```python
len(queue)
```

---

## 🔹 Mental Model

> Keep removing old timestamps until all remaining ones are within the last 3000 ms

---

## 🔹 Important Detail

We check:

```python
queue[0] < t - 3000
```

NOT:

```python
last - first <= 3000 ❌
```

---

## 🔹 Why Queue?

* Oldest elements become invalid first
* We remove from the **front**
* We add to the **back**

👉 FIFO → Queue

---

## 🔹 Complexity

### Time:

* Each element:

  * added once
  * removed once

👉 **O(n) total**

👉 **Amortized O(1) per ping**

---

### Space:

* At most all elements in a 3000ms window

👉 **O(n)** worst case

---

## 🔹 Mistakes You Made

### 1. ❌ Thinking in terms of first vs last difference

You thought:

```text
last - first <= 3000
```

Correct:

```text
keep values in [t - 3000, t]
```

---

### 2. ❌ Not fully understanding what we store

You assumed:

* we store all timestamps

Reality:

> we only store **valid (recent) timestamps**

---

### 3. ❌ Missing the “cleaning” idea

Key idea is:

> we continuously **clean old elements**

---

## 🔹 What You Learned

* Sliding window doesn’t always use two pointers
* It can be implemented with a **queue**
* You don’t need to scan everything every time
* `while` loop here is NOT O(n²)

---

## 🔹 Interview Notes

### ✅ Use `deque`

* Correct and expected
* Using list with `pop(0)` is bad (O(n))

---

### ✅ What to say

> “We maintain a sliding window of timestamps within the last 3000 ms using a queue.
> We remove outdated timestamps from the front and return the size.”

---

### ✅ Bonus (strong signal)

> “Each element is added and removed once → amortized O(1) per operation”

---

## 🔹 Final Takeaway

> This problem is about maintaining a **valid window of data**, not recalculating it.
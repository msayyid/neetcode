# 📝 Design Circular Queue - Notes

---

# 1. Brute Force Approach (Your First Version)

## Idea

* Use a fixed-size list: `[None] * k`
* Treat `None` as empty space
* Scan the array to:

  * find insertion point
  * find front/rear
  * check empty/full

---

## Operations

### enQueue

* Check if full (`no None`)
* Find first `None`
* Insert value there

⏱ Time: O(n)

---

### deQueue

* Find first non-None (front)
* Remove it (`set to None`)
* Shift everything left
* Set last index to `None`

⏱ Time: O(n)

---

### Front

* Scan left → right
* Return first non-None

⏱ Time: O(n)

---

### Rear

* Scan right → left
* Return last non-None

⏱ Time: O(n)

---

### isEmpty / isFull

* Scan entire array

⏱ Time: O(n)

---

## Problems with this approach

* ❌ Requires scanning every time
* ❌ Requires shifting (expensive)
* ❌ Not truly “circular”
* ❌ Doesn’t reuse freed space efficiently (conceptually)

---

## Mistakes / Struggles You Had

### 1. Confusion about fixed-size arrays in Python

* Learned: simulate using `[None] * k`

---

### 2. Not knowing where to insert/remove

* You relied on scanning instead of tracking position

---

### 3. Dequeue direction mistake

* Initially removed from **rear instead of front**
* Fixed by switching to left-to-right scan

---

### 4. Shifting logic confusion

* Main challenge:

```text
[None, 2, 3, None] → [2, 3, None, None]
```

* Learned how to shift using loop

---

## Key Takeaways

* You *can* simulate queue with array + scanning
* But:

```text
Scanning = slow
Shifting = bad
```

👉 This approach is correct but not optimal

---

# 2. Optimal Circular Queue (Final Version)

## Idea

Use:

* Fixed array
* Two pointers:

  * `front` → first element
  * `rear` → last element
* `size` → track number of elements
* Modulo `% k` → wrap around

---

## Core Concept

👉 No scanning
👉 No shifting
👉 Always know where to insert/remove

---

## Operations

### enQueue

Steps:

1. Check if full (`size == k`)
2. Move rear:

```text
rear = (rear + 1) % k
```

3. Insert value
4. Increase size

⏱ Time: O(1)

---

### deQueue

Steps:

1. Check if empty (`size == 0`)
2. Remove at front
3. Move front:

```text
front = (front + 1) % k
```

4. Decrease size

⏱ Time: O(1)

---

### Front

* Return `queue[front]` if not empty

⏱ Time: O(1)

---

### Rear

* Return `queue[rear]` if not empty

⏱ Time: O(1)

---

### isEmpty / isFull

```text
isEmpty → size == 0
isFull  → size == k
```

⏱ Time: O(1)

---

## Modulo Insight (Your Key Learning Point)

```text
(index + 1) % k
```

means:
👉 move forward
👉 wrap to 0 if needed

Example:

```text
(4 + 1) % 5 = 0
```

---

## Why This Works

* Avoids shifting
* Reuses freed space
* Maintains order (FIFO)
* Efficient

---

## Mistakes / Struggles You Had

### 1. Confusion about rear logic

* Initially inserted before moving rear
* Fixed by:

```text
move → then insert
```

---

### 2. Missing `self.` errors

* Common Python mistake

---

### 3. Modulo confusion

* Didn’t fully understand wrap-around
* Now clear:
  👉 modulo = circular movement

---

### 4. Thinking in “search mode”

* Initially:

```text
find first None
```

* Now:

```text
I KNOW where to insert
```

👉 This is the biggest mindset shift

---

## Key Takeaways

### 🔑 Core pattern

```text
rear = (rear + 1) % k
front = (front + 1) % k
```

---

### 🔑 Track size instead of scanning

```text
size == 0 → empty
size == k → full
```

---

### 🔑 No shifting ever

That’s the whole point of circular queue

---

# Final Comparison

| Feature       | Brute Force | Optimal |
| ------------- | ----------- | ------- |
| Insert        | O(n)        | O(1)    |
| Delete        | O(n)        | O(1)    |
| Front/Rear    | O(n)        | O(1)    |
| Uses shifting | Yes         | No      |
| Uses scanning | Yes         | No      |
| Interview     | ❌           | ✅       |

---

# Final Insight (Important)

Your progression was perfect:

```text
Scan → Understand → Optimize → Use pointers
```

👉 That’s exactly how strong problem solving develops.
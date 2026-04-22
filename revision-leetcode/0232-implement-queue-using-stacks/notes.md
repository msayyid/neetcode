# 232. Implement Queue using Stacks - Notes

## Core Idea

We need to simulate a **queue (FIFO)** using **stacks (LIFO)**.

To achieve this, we use **two stacks**:

* `stack1` (in_stack) - for pushing elements
* `stack2` (out_stack) - for popping/peeking elements

---

## Key Insight

A stack reverses order.

So if we:

1. Push elements into `stack1`
2. Move them into `stack2`

👉 Order gets reversed → behaves like a queue

---

## How Operations Work

### push(x)

* Always push into `stack1`

---

### pop()

* If `stack2` is empty:

  * Move all elements from `stack1` → `stack2`
* Pop from `stack2`

---

### peek()

* Same as pop, but return top of `stack2` instead of removing

---

### empty()

* Queue is empty only if:

  ```python
  not stack1 and not stack2
  ```

---

## Why Transfer Only When Needed?

We **delay reversal** until required.

This avoids unnecessary work and ensures efficiency.

---

## Time Complexity

| Operation | Complexity     |
| --------- | -------------- |
| push      | O(1)           |
| pop       | amortized O(1) |
| peek      | amortized O(1) |
| empty     | O(1)           |

---

## Amortized Analysis (IMPORTANT)

* Each element:

  * pushed once → O(1)
  * moved once → O(1)
  * popped once → O(1)

👉 Total per element = O(1)

👉 Over n operations = O(n)

👉 Per operation = **O(1) amortized**

---

## Common Mistakes (you made)

### 1. Using list as queue

```python
pop(0)
```

* ❌ O(n) due to shifting

---

### 2. Reversing on every push

```python
self.out_stack = reversed(self.in_stack)
```

* ❌ wrong logic
* ❌ not a stack
* ❌ inefficient

---

### 3. Not understanding when to transfer

* Transfer should happen **only when `stack2` is empty**

---

### 4. Wrong empty condition

* Must check **both stacks**

---

## Key Takeaways

* Queue = FIFO, Stack = LIFO → need reversal
* Use **lazy transfer** (only when needed)
* Amortized thinking is important in interviews
* Avoid operations like `pop(0)` in arrays

---

## Interview Summary (what to say)

> Use two stacks. Push into stack1. For pop/peek, if stack2 is empty, transfer elements from stack1 to stack2 to reverse order. Each element is moved at most once, so operations are O(1) amortized.

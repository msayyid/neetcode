# 1. Brute Force Approach

## Idea

For each day:

* Look forward until you find a warmer temperature
* Count how many days it takes

---

## Steps

* Loop through each index `i`
* For each `i`, loop from `i+1 → end`
* If `temperatures[j] > temperatures[i]`

  * answer[i] = j - i
  * stop inner loop
* If none found → answer[i] stays 0

---

## Time Complexity

* Outer loop: O(N)
* Inner loop: O(N)
  👉 Total: **O(N²)**

---

## Space Complexity

* Answer array: O(N)
  👉 Total: **O(N)**

---

## Problems with this approach

* Repeats work many times
* Slow for large inputs (TLE)

---

## Key Learning

* Nested loops over large arrays → usually too slow
* Need to avoid re-checking the same elements

---

# 2. Stack (Monotonic Stack) Approach

## Core Idea

* Keep track of days that are still waiting for a warmer temperature
* Use a stack to store their indexes

---

## What the stack stores

* **Indexes of days**
* These days are unresolved (no warmer day found yet)

---

## Steps

* Loop from left → right
* For each day `i`:

  * While stack is not empty AND current temp is higher:

    * Pop previous day
    * Calculate wait:

      ```
      answer[prev] = i - prev
      ```
  * Push current index to stack

---

## Why it works

* Each day is:

  * pushed once
  * popped once
    👉 No repeated work

---

## Time Complexity

* Each element pushed once → O(N)
* Each element popped once → O(N)
  👉 Total: **O(N)**

---

## Space Complexity

* Answer array: O(N)
* Stack: worst case O(N)
  👉 Total: **O(N)**

---

## Key Insight

👉 “Resolve previous days when a warmer day appears”

---

## Pattern Name

* **Monotonic Decreasing Stack**

  * Stack keeps temperatures in decreasing order

---

## Why `while` (not `if`)

* One day can resolve multiple previous days

---

## Edge Case Insight

* If no warmer day exists:

  * element stays in stack
  * answer remains 0

---

## Common Mistakes

* Storing temperatures instead of indexes
* Forgetting `while` (using `if` instead)
* Mixing up `i - prev` direction

---

## Key Learning

* Avoid brute force by storing unresolved states
* Stack helps process each element only once

---

# Final Comparison

| Approach    | Time  | Space | Notes                |
| ----------- | ----- | ----- | -------------------- |
| Brute Force | O(N²) | O(N)  | Simple but slow      |
| Stack       | O(N)  | O(N)  | Optimal and expected |

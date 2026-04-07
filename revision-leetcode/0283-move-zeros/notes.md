**LeetCode 283 - Move Zeroes**

---

### Problem

Move all `0`s to the end of the array while maintaining the **relative order** of non-zero elements.
Must be done **in-place** (no extra array).

---

### Key Insight

This is **not a swapping problem**.
This is a **stable compaction problem**:

* Keep non-zero elements in order
* Push them forward
* Fill the rest with zeros

---

### Correct Approach (Two Pointers - Insert Position)

We use:

* `i` → scans the array
* `insert_pos` → where the next non-zero should go

**Logic:**

1. Iterate through the array
2. If element is non-zero:

   * Place it at `insert_pos`
   * Increment `insert_pos`
3. After loop → fill remaining positions with `0`

---

### Important Optimization

We add:

> Only move when needed

Condition:
`i != insert_pos`

---

### Why do we use `i != insert_pos`?

Simple idea:

> Check if the number is already in the correct position.

* If `i == insert_pos` → already correct → **do nothing**
* If `i != insert_pos` → needs to move → **move it**

This avoids unnecessary writes like:

* `nums[0] = nums[0]` (useless operation)

---

### Example Walkthrough

Input:
`[0, 1, 0, 3, 12]`

Steps:

* Move `1` to index `0`
* Move `3` to index `1`
* Move `12` to index `2`

Intermediate:
`[1, 3, 12, ?, ?]`

Fill rest with zeros:
`[1, 3, 12, 0, 0]`

---

### Common Mistake (Important)

❌ Using two pointers (left + right) and swapping with the end

Why it fails:

* Breaks order of elements

Example:
`[0,1,0,3,12] → [12,1,0,3,0]` ❌ wrong

---

### Correct Mindset

* Do NOT swap with end
* Do NOT treat it like partitioning
* Think:

  > “Shift non-zero elements forward while keeping order”

---

### Complexity

* Time: O(n)
* Space: O(1)
* Optimal for interviews

---

### Final Takeaways

* This is a **stable shift problem**, not swap
* Preserve order → very important constraint
* `insert_pos` tracks where next valid element goes
* `i != insert_pos` avoids unnecessary work

---

### One-line Summary

> Move non-zero elements forward in order, and fill the rest with zeros.

# Two Sum II - Sorted Array (LeetCode 167)

## Problem Summary

* Given a **sorted array**
* Find **two numbers** that sum to target
* Return **1-based indices**
* Constraints:

  * Exactly **one solution**
  * Must use **O(1) extra space**

---

# Key Insight

Because the array is **sorted**, we can:

> Control the sum by moving pointers intelligently

---

# Approach 1: Two Pointers (Optimal)

## Idea

* Use two pointers:

  * `l` at start (smallest)
  * `r` at end (largest)

* Check sum:

  ```python
  numbers[l] + numbers[r]
  ```

---

## Pointer Movement Logic

* If sum == target → return answer
* If sum < target → need bigger sum → `l += 1`
* If sum > target → need smaller sum → `r -= 1`

---

## Why this works

Because array is sorted:

* Moving `l → right` ⇒ increases value
* Moving `r → left` ⇒ decreases value

So we can **adjust sum deterministically**

---

## Code

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]

            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1
```

---

## Complexity

* Time: **O(n)**
* Space: **O(1)**

---

## Important Properties

* `l < r` is always maintained → correct index order guaranteed
* Never revisit elements → single pass
* Eliminates impossible pairs safely

---

## How to explain in interview (simple)

> Start from both ends. If sum is too small, move left pointer to increase it. If too big, move right pointer to decrease it. Since array is sorted, this guarantees we find the correct pair in one pass.

---

# Approach 2: Hashmap (General Two Sum)

## Idea

* For each number `x`
* Check if `target - x` was seen before

---

## Code

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_map = {}

        for i in range(len(numbers)):
            if target - numbers[i] in my_map:
                return [my_map[target - numbers[i]] + 1, i + 1]
            my_map[numbers[i]] = i
```

---

## Key Logic

* Map stores:

  ```python
  value → index
  ```

* Order matters:

  ```python
  [previous_index, current_index]
  ```

---

## Common Mistake

Wrong:

```python
[i + 1, my_map[target - numbers[i]] + 1]
```

Correct:

```python
[my_map[target - numbers[i]] + 1, i + 1]
```

Reason:

* map index is **earlier**
* `i` is **later**
* must return `index1 < index2`

---

## Complexity

* Time: **O(n)**
* Space: **O(n)** ❌ (violates constraint)

---

## Why NOT use hashmap here

* Problem requires:

  > constant extra space

So even though hashmap works:

> It is **not the optimal solution for this problem**

---

# Comparison

| Approach     | Time | Space | Works on Unsorted | Preferred |
| ------------ | ---- | ----- | ----------------- | --------- |
| Two pointers | O(n) | O(1)  | ❌                 | ✅ BEST    |
| Hashmap      | O(n) | O(n)  | ✅                 | ❌ here    |

---

# Key Takeaways

1. **Sorted array → think two pointers first**
2. Two pointers:

   * controls sum using structure
   * guarantees order
3. Hashmap:

   * more general
   * but uses extra space
4. Always match solution to constraints

---

# Mental Model

Think like this:

* Left = small number
* Right = big number

If:

* Too small → move left
* Too big → move right

---

# Edge Cases (handled automatically)

* Negative numbers
* Only 2 elements
* Solution at extremes
* Large input

---

# Final Interview Summary (what you say)

> Since the array is sorted, I use two pointers from both ends. If the sum is too small, I move the left pointer to increase it. If it's too large, I move the right pointer to decrease it. This gives O(n) time and O(1) space, which satisfies the constraint.
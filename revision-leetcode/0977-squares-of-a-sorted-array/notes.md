# 📝 Notes - Squares of a Sorted Array (LeetCode 977)

## Problem

Given a sorted array (non-decreasing), return a new array of squares also sorted.

---

# 🔹 Approach 1 - Brute Force

## Idea

1. Square every element
2. Sort the array again

## Code

```python
for i in range(len(nums)):
    nums[i] = nums[i] * nums[i]

nums.sort()
return nums
```

## Complexity

* Time: `O(n log n)` (because of sorting)
* Space: `O(1)` (in-place)

## Key Point

* Sorting is the expensive step
* Works but not optimal

---

# 🔹 Approach 2 - Two Pointers (Optimal)

## 💡 Core Idea

* Largest square comes from either:

  * left (big negative)
  * right (big positive)

So:
👉 Compare both ends
👉 Put the bigger square at the **end of result array**

---

## 🧠 Mental Model

```
[-7, -3, 2, 3, 11]

Squares:
[49, 9, 4, 9, 121]

Biggest values are at the EDGES
```

So we:

* take biggest first
* fill result from BACK → FRONT

---

## Algorithm Steps

1. `l = 0`, `r = n - 1`
2. Create `res = [0] * n`
3. Use `index = n - 1` (position to fill)
4. Loop while `l <= r`:

   * compare `abs(nums[l])` and `abs(nums[r])`
   * put bigger square into `res[index]`
   * move pointer
   * decrease index

---

## Code

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        index = len(nums) - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[index] = nums[l] * nums[l]
                l += 1
            else:
                res[index] = nums[r] * nums[r]
                r -= 1
            index -= 1

        return res
```

---

## Complexity

* Time: `O(n)`
* Space: `O(n)`

---

# ⚠️ Mistakes I Made

### 1. Tried to “fix negatives first”

* Thought about shifting negatives
* ❌ unnecessary and complex

👉 Better: build result instead of modifying input

---

### 2. Thought about comparing with previous squared value

* ❌ not needed

👉 Always compare:

```
abs(nums[l]) vs abs(nums[r])
```

---

### 3. Used `while l < r`

* ❌ missed last element

👉 Correct:

```
while l <= r
```

---

# 🔑 Important Concept - “index / pos variable”

## What it is

A pointer that tracks **where to insert in result array**

```python
index = n - 1
```

## Why we need it

* We are placing **largest values first**
* So we must fill from the **end**

## How it works

Every iteration:

```
res[index] = value
index -= 1
```

## Insight

👉 This is a common pattern:

> “When building result in reverse order, use a separate index pointer”

---

# 🧠 Pattern Recognition

This problem teaches:

### 1. Two Pointers on Sorted Array

* use both ends when transformation breaks order

### 2. Build Output Instead of Modifying Input

* avoids complexity

### 3. Reverse Filling Trick

* when largest comes first → fill from back

---

# 🔥 Interview Sentence

> “Since the largest square comes from either end, I use two pointers and fill the result array from the back in O(n).”

---

If you remember just this:

* compare ends
* fill from back
* move pointer

you’ll solve this instantly next time.

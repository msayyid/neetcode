# 905. Sort Array By Parity

### Problem
Given an integer array `nums`, move all even integers to the beginning and all odd integers to the end. Return any valid arrangement (order within evens/odds doesn't matter).

### Pattern
**Two Pointers — opposite ends, partition by predicate.** Same family as Dutch National Flag, Move Zeroes, and the partition step in quicksort. Whenever you need to rearrange an array into two groups in-place without caring about the relative order within each group, two pointers from opposite ends is the go-to.

### Idea
Walk one pointer `i` from the left and another pointer `j` from the right. Left pointer's job: find an odd number (something that shouldn't be on the left). Right pointer's job: find an even number (something that shouldn't be on the right). When both pointers are stuck on a "wrong" element, swap them. Repeat until the pointers meet — at that point the array is partitioned.

### Pseudocode
```
i ← 0
j ← len(nums) - 1
while i < j:
    if nums[i] is even:
        i += 1                  # already in correct (left) zone
    else if nums[j] is odd:
        j -= 1                  # already in correct (right) zone
    else:
        # nums[i] is odd, nums[j] is even — both misplaced
        swap nums[i] and nums[j]
        i += 1
        j -= 1
return nums
```

### Mistakes I made / things I learned
- **My first version used three separate `if` statements instead of `if / elif / else`.** This meant multiple branches could fire in a single iteration. It happened to still produce correct output, but the control flow was doing more work than intended — each iteration of a two-pointer loop should logically do *one* thing: advance `i`, retreat `j`, or swap. Using `elif` makes those cases mutually exclusive, which matches the intent.
- **I had a redundant condition in the last branch.** I wrote `elif nums[i] % 2 == 1 and nums[j] % 2 == 0` for the swap case, but by the time control reaches that branch, both conditions are *already guaranteed* by the previous branches being false. So it should just be `else`.
- **Loop condition was `i <= j` but should be `i < j`.** When `i == j` the two pointers are looking at the same single element — there's nothing to swap with itself, and the branches that advance/retreat would just push them past each other unnecessarily. Tighter bound is `i < j`.
- **Pythonic evenness check:** `n % 2 == 0` works, but `not n % 2` (and `n % 2` for odd) is cleaner because `0` is falsy and `1` is truthy in Python.

### Complexity
- **Time: O(n)** — each pointer moves at most n/2 steps; together they cover the array exactly once.
- **Space: O(1)** — swaps happen in place, no extra structure.

### Final code
```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0:
                i += 1
            elif nums[j] % 2 == 1:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums
```
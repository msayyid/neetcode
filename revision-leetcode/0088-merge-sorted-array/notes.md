## LeetCode 88 - Merge Sorted Array Notes

### Problem idea

You are given two sorted arrays:

```python
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
```

Only the first `m` elements of `nums1` are real.

The last `n` zeroes in `nums1` are just empty space for merging.

Goal: merge `nums2` into `nums1` in-place.

---

## Key trick

Merge from the back, not from the front.

Why?

Because `nums1` already has empty spaces at the end.

So we can place the biggest remaining number at the back without overwriting useful values.

---

## Pointer setup

```python
i = m + n - 1      # position where we place the next biggest value
left = m - 1       # last real element in nums1
right = n - 1      # last element in nums2
```

Example:

```python
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
```

Pointers:

```text
nums1: [1, 2, 3, 0, 0, 0]
              L        i

nums2: [2, 5, 6]
              R
```

---

## Main logic

Compare:

```python
nums1[left] vs nums2[right]
```

Put the larger value into:

```python
nums1[i]
```

Then move the pointer of the value you used.

---

## Correct loop condition

```python
while right >= 0:
```

Why not `while left >= 0 or right >= 0`?

Because if `nums2` is finished, the remaining `nums1` values are already in the correct place.

But if `nums1` is finished first, we still need to copy the remaining `nums2` values into `nums1`.

---

## Important condition

```python
if left >= 0 and nums1[left] > nums2[right]:
```

The `left >= 0` check is important.

Without it, Python may access `nums1[-1]`, which means the last element, causing wrong logic.

Also, use:

```python
left >= 0
```

not:

```python
left > 0
```

Because index `0` is valid and must still be checked.

---

## Final solution

```python
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m + n - 1
        left = m - 1
        right = n - 1

        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[i] = nums1[left]
                left -= 1
            else:
                nums1[i] = nums2[right]
                right -= 1

            i -= 1
```

---

## Example dry run

Input:

```python
nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
```

Start:

```text
i = 1
left = 0
right = 0
```

Compare:

```text
nums1[left] = 2
nums2[right] = 1
```

Since `2 > 1`, place `2` at `nums1[i]`.

```python
nums1 = [2, 2]
```

Move pointers:

```text
i = 0
left = -1
right = 0
```

Now `left` is invalid, so copy from `nums2`.

```python
nums1[0] = nums2[0]
```

Final:

```python
nums1 = [1, 2]
```

---

## Common mistakes

### Mistake 1: Using `left > 0`

Wrong:

```python
if left > 0:
```

Correct:

```python
if left >= 0:
```

Index `0` is still valid.

---

### Mistake 2: Merging from the front

If you merge from the front, you may overwrite useful values in `nums1`.

That is why merging from the back is safer.

---

### Mistake 3: Swapping with `nums2`

You do not need to swap anything.

Just write the correct value into `nums1[i]`.

---

## Complexity

Time complexity:

```text
O(m + n)
```

Each element is processed at most once.

Space complexity:

```text
O(1)
```

No extra array is used.

---

## Interview takeaway

This is the expected optimal solution.

The main insight is:

> Because `nums1` has empty space at the end, fill it from right to left using the largest remaining value.

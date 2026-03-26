# 3Sum — Notes

## Problem
Given an integer array `nums`, return all **unique triplets** `[nums[i], nums[l], nums[r]]` such that:
`nums[i] + nums[l] + nums[r] == 0`

---

## Where I started — Brute Force O(n³)
My first attempt tried every combination of i, j, k with three nested loops. It had two bugs:
- `temp` was defined outside the loop so it accumulated across iterations
- I was checking the sorted version of `temp` for duplicates but appending the unsorted version to `res`

Even after fixing those, O(n³) times out on large inputs.

---

## The Idea — Sort + Fix + Two Pointers

1. Sort the array
2. Fix one element at index `i` with an outer loop
3. Use two pointers `l = i+1` and `r = n-1` to find two numbers that sum to `-nums[i]`

For each `i`, we are essentially solving a 2Sum problem on the remaining sorted subarray.

### Why sorting enables two pointers
As I put it during our session: *"the righter the pointer the bigger the number"* — that is the entire intuition.

- If `cur_sum < 0` → too small, move `l` right to get a bigger number
- If `cur_sum > 0` → too large, move `r` left to get a smaller number

### Why this covers all triplets
The outer loop gives every element a turn as `nums[i]`. For each `i`, the two pointers exhaustively scan all remaining pairs. After sorting we know `nums[i] <= nums[l] <= nums[r]` always, so unlike the brute force we do not need to check every ordering.

---

## Duplicate Handling — The Trickiest Part

Three places to skip duplicates:

**1. Skip duplicate `i` values**
If `nums[i] == nums[i-1]`, we already used this value as the first number — skip it.
Always guard with `i > 0` first, otherwise `nums[-1]` wraps around to the last element.

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

**2. Skip duplicate `l` values after a valid triplet**
Move `l` first, then skip while the new value equals the old one.

```python
l += 1
while l < r and nums[l] == nums[l - 1]:
    l += 1
```

**3. Skip duplicate `r` values after a valid triplet**
Must decrement `r` first, then compare with `r+1`. Doing it the other way around accesses an out-of-bounds index.

```python
r -= 1
while r > l and nums[r] == nums[r + 1]:
    r -= 1
```

---

## Mistakes Made Along The Way
- `temp` not reset inside the loop — accumulated across iterations
- Appending unsorted triplet but checking sorted one for duplicates
- Used `range(1, n)` which skipped `i=0` entirely
- Short-circuit order: `nums[i] == nums[i-1] and i > 0` — Python evaluates left to right so `nums[-1]` was accessed when `i=0`. Guard must come first
- Same short-circuit issue for the `l` and `r` while loops
- For `r` duplicates: checked `nums[r] == nums[r+1]` before moving `r` — out of bounds. Must decrement first

---

## Small Optimisation
```python
if nums[i] > 0:
    break
```
Since the array is sorted, if `nums[i]` is already positive then everything to its right is also positive. Three positive numbers can never sum to zero.

---

## Final Code

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            l, r = i + 1, n - 1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if cur_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1

                elif cur_sum > 0:
                    r -= 1
                else:
                    l += 1

        return res
```

---

## Pseudocode

```
sort nums

for i from 0 to n-3:
    if i > 0 and nums[i] == nums[i-1]: skip
    if nums[i] > 0: break

    l = i+1, r = n-1

    while l < r:
        cur_sum = nums[i] + nums[l] + nums[r]

        if cur_sum == 0:
            save triplet
            l += 1, skip duplicate l values
            r -= 1, skip duplicate r values

        elif cur_sum < 0: l += 1
        else: r -= 1

return res
```

---

## Dry Run

Input: `[-1, 0, 1, 2, -1, -4]`
After sorting: `[-4, -1, -1, 0, 1, 2]`

- `i=0, nums[i]=-4` → all sums too small, no triplet
- `i=1, nums[i]=-1` → finds `[-1,-1,2]` then `[-1,0,1]`
- `i=2, nums[i]=-1` → duplicate of previous `i`, skip
- `i=3, nums[i]=0` → `0+1+2=3` too large, move `r`, `l` meets `r`, done

Result: `[[-1,-1,2], [-1,0,1]]`

---

## Complexities

| | Complexity |
|---|---|
| Time | O(n²) — outer loop O(n), two pointers O(n) each. Sorting O(n log n) is dominated |
| Space | O(1) extra ignoring output. Sorting 3 elements in brute force was also O(1) — fixed-size sorts are always negligible |

---

## How To Explain In An Interview
"I sort the array so I can use two pointers. I fix one number at index `i`, then use `l` and `r` to find two numbers that sum to `-nums[i]`. If the sum is too small I move `l` right, if too large I move `r` left. When I find a valid triplet I skip duplicate values on both sides. I also skip duplicate `i` values so the result only has unique triplets."

---

## Key Things To Remember
- Sorting is what makes two pointers possible
- For each `i`, solve 2Sum on the rest with `l` and `r`
- Too small → move `l`. Too big → move `r`
- Skip duplicates in three places: `i`, `l`, `r`
- Guard before comparing: `i > 0` and `l < r` and `r > l` must always come first
- Decrement `r` before checking its duplicate — not after
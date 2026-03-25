**Remove Duplicates from Sorted Array**

**Approach:** Two-pointer (write pointer pattern)

**Key insight:** Use `k` as both a counter and a write pointer — it tracks where to place the next unique element. Since the array is sorted, duplicates are always adjacent, so compare `nums[i]` with `nums[i-1]`.

**What I got wrong initially:**
- Started by only counting unique elements, not modifying the array in-place
- Had a redundant `j` pointer that was always just `i+1`
- Used a fragile end-of-array guard and a `return k+1` to handle the last element
- Tried swapping elements — doesn't work because swapping equal values does nothing

**The clean fix:** Start `k = 1` (first element is always unique, already in place), iterate from index `1`, and compare each element to the one before it. No edge case guards needed.

**Time complexity:** O(n) — single pass  
**Space complexity:** O(1) — in-place, no extra space


```
set k = 1  (first element is always unique)

for i from 1 to end of array:
    if current element != previous element:
        write current element at position k
        increment k

return k
```
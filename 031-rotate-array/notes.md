**Rotate Array - Notes**

**Problem:** Rotate array to the right by `k` steps, in-place.

**Idea:** Use the reversal trick — reverse the whole array, then reverse the first `k` elements, then reverse the remaining elements.

**Pseudocode:**
```
k = k % len(nums)
reverse entire array
reverse nums[0..k-1]
reverse nums[k..n-1]
```

**Mistakes I made:**
- Tried `nums = res` to modify in-place — this just rebinds the local variable, the original list is untouched. To modify in-place, you need to modify the list's **contents** e.g. `nums[:] = res`
- Tried a two-pointer swap approach — it swapped the right elements to the front but left the displaced elements in the wrong order at the back

**New things learnt:**
- `nums = res` vs modifying contents in-place — reassignment never works for in-place problems
- The reversal trick for array rotation
- Always handle `k > len(nums)` with `k = k % n` before doing anything
- Extract repeated logic into a nested helper function to keep code clean

**Time complexity:** O(n) — 3 reversals = O(3n) = O(n)

**Space complexity:** O(1) — all done in-place, no extra data structures

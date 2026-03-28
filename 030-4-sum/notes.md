**4Sum**

**Idea:**
Sort the array, fix two elements with nested loops (`a` and `b`), then use two pointers (`l` and `r`) on the remaining subarray to find pairs that complete the target sum. Sorting enables both duplicate skipping and the two pointer guarantee.

**What sorting gives us:**
- Duplicates become adjacent, so a simple `nums[i] == nums[i-1]` check is enough to skip them
- Every quadruplet is found in sorted order automatically, so no need to sort individual results or check if they already exist in res (which was O(n) per check in brute force)

**Why two pointers works:**
Because the array is sorted, at any moment everything left of `l` is smaller and everything right of `r` is bigger. So:
- Sum too small → moving `r` left makes it worse, must move `l` right
- Sum too big → moving `l` right makes it worse, must move `r` left
- This guarantees no valid pair is ever skipped

**Where we saved a power of n vs brute force:**
The two nested loops for `c` and `d` (O(n²)) were replaced by a single two pointer pass (O(n)), because every step either finds a valid pair or permanently eliminates a candidate.

**Duplicate skipping logic:**
- `a`: skip if `a > 0 and nums[a] == nums[a-1]` — "has a moved at least one step and is same value as before?"
- `b`: skip if `b > a + 1 and nums[b] == nums[b-1]` — threshold is `a + 1` not `1`, because `b` resets its starting position for every new `a`
- `l` and `r` after a valid match: the main loop naturally handles non-duplicates (sum would change), but when sum equals target and both new positions are duplicates, you would append the same quadruplet again — so manual skipping while loops are needed only in the `== target` branch

**Mistakes made:**
- Initially wrote `a == a - 1` and `b == b - 1` (comparing index to index) instead of `nums[a] == nums[a-1]` (comparing values)
- Used `b > 1` as the guard for `b` instead of `b > a + 1` — `b > 1` would incorrectly skip the first valid `b` when `a` is not at index 0

**Pseudocode:**
```
sort nums
for a from 0 to n:
    if a > 0 and nums[a] == nums[a-1]: skip
    for b from a+1 to n:
        if b > a+1 and nums[b] == nums[b-1]: skip
        l = b + 1, r = n - 1
        while l < r:
            sum = nums[a] + nums[b] + nums[l] + nums[r]
            if sum == target:
                append quadruplet
                move l right, skip duplicates
                move r left, skip duplicates
            elif sum < target: move l right
            else: move r left
return res
```

**Time complexity:** O(n³) — O(n²) for the two outer loops, O(n) for two pointer pass, O(n log n) for sorting which is dominated

**Space complexity:** O(k) where k is the number of quadruplets in the result (4 elements each, but 4 is a constant)
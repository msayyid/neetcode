**Two Integer Sum II — Two Pointers**

**Problem:** Given a sorted array, find two indices (1-indexed) whose values sum to target. O(1) space required.

**What I tried first:** A brute force N² nested loop — worked but ignored the sorted property entirely.

**The solution — Two Pointers:** Place one pointer at the start (`l`) and one at the end (`r`). At each step, sum the two values they point at and compare to target. If the sum is too big, move `r` left to get a smaller number. If the sum is too small, move `l` right to get a bigger number. If equal, return the 1-indexed positions. Keep going until they meet.

**Key insight:** Because the array is sorted, we can always make a meaningful decision about which pointer to move — we never need to check every pair.

**Small mistake I made:** I said "the lefter the bigger" — it's actually the opposite. Since the array is non-decreasing, moving **right** gives bigger numbers, moving **left** gives smaller ones.

**Note on the constraint:** `index1 < index2` refers to the **indices**, not the values. Duplicate values at different positions are totally fine.

**Why it always works:** At every step we're either finding the answer or eliminating impossible pairs. Since the problem guarantees exactly one valid solution exists, we will always land on it. No need to handle a "no answer" case.

**Pseudocode:**
```
l = 0, r = end of array
while l < r:
    if numbers[l] + numbers[r] == target → return [l+1, r+1]
    if sum > target → move r left (need smaller number)
    if sum < target → move l right (need bigger number)
```

**Time complexity:** O(n) — we traverse the array at most once

**Space complexity:** O(1) — only two pointers, no extra data structures

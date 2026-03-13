**Longest Consecutive Sequence — Notes**

**Approach 1: Sort + Scan — O(n log n) time, O(1) extra space**

Sort the array, walk through comparing adjacent elements. Three cases for `nums[i] - nums[i-1]`:
- `== 1` → extend streak
- `== 0` → duplicate, falls through naturally
- `> 1` → gap, save streak and reset

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest, count = 0, 1
        for i in range(1, len(nums)):
            comparison = nums[i] - nums[i-1]
            if comparison == 1:
                count += 1
            elif comparison > 1:
                longest = max(longest, count)
                count = 1
        return max(longest, count)
```

**Approach 2: HashSet — O(n) time, O(n) space**

Build a set from nums for O(1) lookups. Loop through nums and for each number check if `n-1` exists in the set — if it doesn't, this number is a sequence start. From the start, count forward by checking if `n + count` exists in the set, incrementing count each time. When the while loop ends, update longest. Numbers that have `n-1` in the set are skipped entirely as they belong to someone else's sequence.

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in numSet:
                count = 0
                while n + count in numSet:
                    count += 1
                longest = max(longest, count)
        return longest
```

**Why O(n) despite nested while loop:** amortized — each number is visited at most twice total. The while loop only runs from sequence starts, not every element.

---

**Mistakes I made:**
- Started `count = 0` instead of `1` in sorted approach — off by one, already standing on a number at start
- Forgot to reset `count` after a gap
- Forgot final `max(longest, count)` — last sequence never hits a gap so never gets saved
- `range(len(nums)+1)` caused index out of bounds
- Empty array guard is necessary in sorted approach because `count = 1` would return 1 for `[]`

**Things I learned:**
- `sorted()` → O(n) space; `.sort()` → O(1) extra space but mutates input — worth flagging in interviews
- Duplicates produce difference `0` after sorting — safe to skip naturally
- Amortized complexity — a nested loop isn't always O(n²), depends on how many times each element is actually touched
- `count` represents *length* not *steps* — at `n + 0` we're already counting `n` itself

**Interview note:** Problem requires O(n), so linear solution is the expected answer. Sorted approach is a great stepping stone to mention first though.
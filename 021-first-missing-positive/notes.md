**First Missing Positive — Brute Force (O(n) time, O(n) space)**

```python
nums_set = set(nums)
count = 1
for i in range(len(nums)):
    if count not in nums_set:
        return count
    count += 1
return count
```

**What I did:**
Put all numbers into a set for O(1) lookup and automatic duplicate removal. Then start `count` at 1 (the smallest possible positive integer) and keep asking "is this number in the set?". If not, we've found our answer. If yes, increment and check the next. If we exhaust the loop, every number 1 to n was present, so the answer is n+1 which is just `count` at that point.

**Mistake I had:**
Originally looped over `nums` and checked `num + 1` — this failed when the array had no positives starting from 1, because the loop never got a chance to check for `1` being missing.

**Why this violates the constraint:**
Space is `O(n)` because the set stores up to n elements. The problem requires `O(1)` auxiliary space.

**Complexities:**
- Time: `O(n)` — building the set is `O(n)`, the loop is `O(n)`
- Space: `O(n)` — the set ❌ violates constraint
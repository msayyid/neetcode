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









Here is a good revision note for **Solution 2**:

## First Missing Positive - Optimal In-place Solution

### Core idea

The first missing positive in an array of length `n` must be in the range:

```python
1 to n + 1
```

So we only care about numbers that are:

* positive
* within the array length

That means for each value `x`:

* its correct index is `x - 1`

Example:

* `1` should be at index `0`
* `2` should be at index `1`
* `3` should be at index `2`

---

### Strategy

Use the array itself like a lookup structure.

For each index:

* if `nums[i]` is a valid number (`1 <= nums[i] <= n`)
* and it is not already in its correct place
* and the target place does not already contain the same value

then swap it into its correct index.

After this rearrangement:

* scan from left to right
* the first index `i` where `nums[i] != i + 1` means `i + 1` is missing

If all positions are correct, return `n + 1`.

---

### Why the duplicate check is needed

This condition:

```python
nums[i] != nums[correct]
```

prevents infinite swapping when duplicates exist.

Example:

```python
[1, 1]
```

Without that check, the algorithm could keep swapping the same values forever.

---

### Why `while` is used instead of `for`

After a swap, the new value at `nums[i]` may also need to be placed.

So:

* if a swap happens, stay on the same index
* if no swap is needed, move to the next index

---

### Final check meaning

This line:

```python
if nums[i] != i + 1:
```

means:

* at index `0`, I expect `1`
* at index `1`, I expect `2`
* at index `2`, I expect `3`

So:

* **placement rule:** value `x` goes to index `x - 1`
* **checking rule:** index `i` should contain value `i + 1`

---

### Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

Even though swaps happen, each valid number is moved toward its correct place, so total work stays linear.

---

### Code

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i < n:
            correct = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
```

### One-line memory trick

**Put each valid number `x` into slot `x - 1`, then find the first index where `nums[i] != i + 1`.**

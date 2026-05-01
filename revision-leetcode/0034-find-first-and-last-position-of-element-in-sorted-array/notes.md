# LeetCode 34: Find First and Last Position of Element in Sorted Array

## Pattern
**Binary Search — Lower Bound & Upper Bound (Find Boundaries of a Target)**

This is the classic "find leftmost / rightmost occurrence" pattern. Use it whenever:
- Array is sorted
- You need the first/last position of something
- O(log n) is required
- Duplicates exist and you need to handle them

Related problems: Search Insert Position, First Bad Version, Find Peak Element, any "find smallest index where condition is true" problem.

## Idea of the Solution

We need TWO binary searches:
1. **First search → leftmost occurrence** of target (lower bound)
2. **Second search → rightmost occurrence** of target (upper bound)

The key insight (in my own words):
> "When we find an element equal to target at `mid`, we don't know if it's THE answer — there might be another target to the left (for leftmost) or right (for rightmost). So we keep mid in the window and keep searching."

That's why the update rule is `right = mid` (not `mid - 1`) for leftmost, and `left = mid` (not `mid + 1`) for rightmost. We don't discard `mid` because it could be our answer.

## The Two Mistakes I Made / Things I Learnt

### Mistake 1: Infinite loop in the rightmost search
- I had `mid = (left + right) // 2` and `left = mid` for the rightmost search.
- When `left = 4, right = 5`: `mid = 4`, then `left = mid = 4`. **No progress → infinite loop.**
- Floor division biases `mid` toward `left`. So when the update is `left = mid`, mid never moves past left.

### Fix: Round `mid` UP for rightmost search
- `mid = (left + right + 1) // 2` makes mid lean toward `right`.
- Now when `left = 4, right = 5`: `mid = 5`, `left = mid = 5`, loop exits. ✓

### The Pattern (memorize!)
| Search type   | mid formula                  | Update rules                     |
|---------------|------------------------------|----------------------------------|
| Leftmost      | `(left + right) // 2`        | `right = mid`, `left = mid + 1`  |
| Rightmost     | `(left + right + 1) // 2`    | `left = mid`, `right = mid - 1`  |

**Rule of thumb:** Whichever pointer gets assigned `mid` (without ±1), make `mid` lean *away* from it. Otherwise → infinite loop.

## Why the post-loop check matters
After each loop, I check `if nums[left] == target` because:
- The loop only narrows the window — it doesn't guarantee target exists.
- For single-element arrays (`nums = [1]`), the loop body never runs, but the check confirms the answer.
- For target not in array, the check correctly leaves `result` as `[-1, -1]`.

## Why the `if not nums` guard is needed
Without it, `nums = []` causes `nums[left]` → `nums[0]` → IndexError after the loop.

## Pseudocode
```
function searchRange(nums, target):
    result = [-1, -1]
    if nums is empty: return result

    # ----- Find leftmost occurrence -----
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2          # round DOWN
        if nums[mid] >= target:
            right = mid                     # keep mid (could be answer)
        else:
            left = mid + 1                  # discard left half
    if nums[left] == target:
        result[0] = left

    # ----- Find rightmost occurrence -----
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right + 1) // 2      # round UP (avoid infinite loop)
        if nums[mid] <= target:
            left = mid                      # keep mid (could be answer)
        else:
            right = mid - 1                 # discard right half
    if nums[left] == target:
        result[1] = left

    return result
```

## Complexity
- **Time:** O(log n) — two binary searches, each O(log n)
- **Space:** O(1) — only a few pointers

## Edge Cases Verified
- `nums = []` → `[-1, -1]` (handled by guard)
- `nums = [1], target = 1` → `[0, 0]` (loop doesn't run, post-check saves us)
- `nums = [2, 2], target = 2` → `[0, 1]`
- `nums = [5,7,7,8,8,10], target = 6` → `[-1, -1]` (post-check catches it)

## Interview Tip
Mention you could refactor the two loops into a helper function (`find_bound(leftmost: bool)`) to DRY up the code, but the two-loop version is more readable and easier to explain on a whiteboard.
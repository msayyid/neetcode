# Maximum Array Correlation

## Pattern
Greedy + Sorting + Two Pointers

## Problem
Given two arrays `a` and `b`, rearrange `b` to maximise the sum
of `b[i]` where `b[i] > a[i]`.

## Intuition
- We want to maximise the SUM of winning values, not the number of wins.
- Sort both arrays in descending order.
- Process the largest values of `b` first because they contribute more.
- Match each `b` with the largest available `a` it can beat.
- This preserves smaller targets for smaller values of `b`.

## Algorithm
1. Sort both arrays in descending order.
2. Use two pointers:
   - `i` tracks the current target in `a`.
   - `bi` tracks the current value in `b`.
3. If `b[bi] <= a[i]`:
   - Skip `a[i]` by incrementing `i`.
   - No remaining `b` can beat this target because `b` is descending.
4. Otherwise:
   - Add `b[bi]` to `total`.
   - Increment both pointers because both elements are used.
5. Stop when either array is exhausted.

## Code

```python
def getMaxArrayCorrelation(a: list[int], b: list[int]) -> int:
    a.sort(reverse=True)
    b.sort(reverse=True)

    i = 0
    bi = 0
    total = 0

    while bi < len(b):
        # No remaining b can beat a[i], so skip this target
        while i < len(a) and b[bi] <= a[i]:
            i += 1

        if i == len(a):
            break

        # Match b[bi] with the largest target it can beat
        total += b[bi]
        bi += 1
        i += 1

    return total
```

## Complexity
- Time: O(n log n) — sorting dominates; two-pointer scan is O(n).
- Space: O(n) worst case for Python sorting.

## Key Greedy Insight
If the largest remaining `b` cannot beat `a[i]`, no smaller `b`
can beat it either. Therefore, safely skip that target.

## Recognition Rule
- Maximise NUMBER of wins → Advantage Shuffle.
- Maximise SUM of winning values → Prioritise larger winning values.
- Rearranging elements to optimise comparisons → Consider sorting
  and greedy two pointers.
## LeetCode 1200 - Minimum Absolute Difference

### Problem idea

Given an array of distinct integers, return all pairs of numbers that have the smallest absolute difference.

Each pair must be:

```text
[a, b]
```

where:

```text
a < b
```

and:

```text
b - a = minimum difference
```

---

## Key observation

The closest numbers will always be next to each other after sorting.

Example:

```python
arr = [4, 2, 1, 3]
```

After sorting:

```python
[1, 2, 3, 4]
```

Now we only need to compare adjacent pairs:

```text
1 and 2
2 and 3
3 and 4
```

We do not need to compare every possible pair.

---

## Approach

1. Sort the array.
2. Set `min_diff` to infinity.
3. Loop through the sorted array and find the smallest difference between adjacent numbers.
4. Loop again and collect all adjacent pairs that have that minimum difference.
5. Return the result.

---

## Why sorting helps

Without sorting, checking every pair would take:

```text
O(n²)
```

After sorting, the minimum difference can only happen between neighbouring elements.

So we reduce the comparison part to:

```text
O(n)
```

The full solution becomes:

```text
O(n log n)
```

because sorting dominates.

---

## Complexity

### Time complexity

Sorting:

```text
O(n log n)
```

Two loops:

```text
O(n) + O(n)
```

Total:

```text
O(n log n)
```

---

### Space complexity

The result list can store up to `n - 1` pairs.

So output space is:

```text
O(m)
```

where `m` is the number of result pairs.

Worst case:

```text
O(n)
```

Python’s `arr.sort()` sorts in-place, but internally it may still use extra memory because Python uses Timsort.

For interviews, you can say:

```text
O(m) output space
```

or more precisely:

```text
O(n) including sorting internals and output
```

---

## Mistake to avoid

Do not compare every pair using nested loops.

Example of slow approach:

```python
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        ...
```

That would be:

```text
O(n²)
```

Too slow for:

```text
n <= 100000
```

---

## Interview explanation

I would explain it like this:

> First, I sort the array because the closest values will be adjacent in sorted order. Then I scan once to find the minimum adjacent difference. After that, I scan again to collect all adjacent pairs with that difference. Sorting takes O(n log n), and the scans take O(n), so the total time complexity is O(n log n).

---

## Final takeaway

This is the expected interview solution.

The important trick is:

```text
Minimum absolute difference is found between adjacent elements after sorting.
```

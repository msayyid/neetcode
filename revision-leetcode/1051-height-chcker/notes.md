# LeetCode 1051 - Height Checker Notes

## Problem idea

We are given:

```python
heights = [1, 1, 4, 2, 1, 3]
```

Students should be standing in **non-decreasing order**, meaning sorted from smallest to largest.

So the expected order is:

```python
expected = [1, 1, 1, 2, 3, 4]
```

We need to count how many positions are different between `heights` and `expected`.

---

# Approach 1 - Sort and compare

## Idea

The simplest way is:

1. Sort the original array.
2. Compare each index with the original array.
3. Count mismatches.

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)

        mismatch = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch += 1

        return mismatch
```

## Example

```python
heights  = [1, 1, 4, 2, 1, 3]
expected = [1, 1, 1, 2, 3, 4]
```

Compare index by index:

```text
index 0: 1 == 1
index 1: 1 == 1
index 2: 4 != 1  mismatch
index 3: 2 == 2
index 4: 1 != 3  mismatch
index 5: 3 != 4  mismatch
```

Answer:

```python
3
```

## Time complexity

Sorting takes:

```text
O(n log n)
```

Comparing takes:

```text
O(n)
```

Overall:

```text
O(n log n)
```

## Space complexity

`sorted(heights)` creates a new array:

```text
O(n)
```

---

# Approach 2 - Counting sort style

## Why counting sort works here

The constraints say:

```text
1 <= heights[i] <= 100
```

So heights can only be between `1` and `100`.

That means we can count how many times each height appears.

Example:

```python
heights = [1, 1, 4, 2, 1, 3]
```

The counts are:

```text
1 appears 3 times
2 appears 1 time
3 appears 1 time
4 appears 1 time
```

So the sorted order must be:

```python
[1, 1, 1, 2, 3, 4]
```

---

# Approach 2A - Build expected manually, then compare

## Code

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 100

        # Step 1: count each height
        for h in heights:
            count[h - 1] += 1

        expected = []

        # Step 2: rebuild sorted order from count
        for i in range(100):
            for _ in range(count[i]):
                expected.append(i + 1)

        # Step 3: compare original with expected
        mismatch = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch += 1

        return mismatch
```

## Important detail

Because array indexes start at `0`, but heights start at `1`:

```python
count[h - 1] += 1
```

So:

```text
height 1 is stored at count[0]
height 2 is stored at count[1]
height 3 is stored at count[2]
...
height 100 is stored at count[99]
```

When rebuilding the expected array:

```python
expected.append(i + 1)
```

Because:

```text
i = 0 means height 1
i = 1 means height 2
i = 2 means height 3
```

---

# Approach 2B - Compare directly without building expected

## Idea

Instead of building the full `expected` array, we can compare immediately while generating the sorted order.

This saves space.

## Code using `for`

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 100

        # Step 1: count each height
        for h in heights:
            count[h - 1] += 1

        mismatch = 0
        original_index = 0

        # Step 2: generate sorted order one value at a time
        for i in range(100):
            for _ in range(count[i]):

                expected_height = i + 1

                if heights[original_index] != expected_height:
                    mismatch += 1

                original_index += 1

        return mismatch
```

## Why this works

This line:

```python
for _ in range(count[i]):
```

means:

> Use this height as many times as it appeared.

Example:

```python
heights = [1, 1, 4, 2, 1, 3]
```

Counts:

```text
1 appears 3 times
2 appears 1 time
3 appears 1 time
4 appears 1 time
```

The loop generates:

```text
1, 1, 1, 2, 3, 4
```

But instead of storing this into `expected`, we compare each generated value directly with the original array.

So this:

```python
if heights[original_index] != expected_height:
```

is like saying:

```python
if heights[i] != expected[i]:
```

except we never actually create `expected`.

---

# For loop vs while loop

Both versions do the same job.

## For loop version

```python
for _ in range(count[i]):
    ...
```

Meaning:

```text
Repeat this height exactly count[i] times.
```

This is cleaner because we do not need to modify the count array.

---

## While loop version

```python
while count[i] > 0:
    ...
    count[i] -= 1
```

Meaning:

```text
Keep using this height until its count becomes 0.
```

This also works, but it changes the count array.

I prefer the `for` loop version here because it is simpler and cleaner.

---

# Final preferred solution

```python
from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 100

        for h in heights:
            count[h - 1] += 1

        mismatch = 0
        original_index = 0

        for i in range(100):
            for _ in range(count[i]):
                expected_height = i + 1

                if heights[original_index] != expected_height:
                    mismatch += 1

                original_index += 1

        return mismatch
```

---

# Time and space complexity

## Sorting approach

```text
Time:  O(n log n)
Space: O(n)
```

Because we create a sorted copy of the array.

---

## Counting sort approach with expected array

```text
Time:  O(n + 100) -> O(n)
Space: O(n)
```

Because:

```text
count array = O(100) = O(1)
expected array = O(n)
```

---

## Counting sort approach without expected array

```text
Time:  O(n + 100) -> O(n)
Space: O(1)
```

Because:

```text
count array size is always 100
```

So it is constant space.

---

# My mistakes

## 1. I built the count array correctly, but was unsure how to rebuild `expected`

The key realization:

```python
count[i]
```

tells us how many times height `i + 1` should appear in sorted order.

So:

```python
for _ in range(count[i]):
    expected.append(i + 1)
```

rebuilds the sorted array.

---

## 2. I created `expected = []` even when I did not use it

In the optimized version, I do not need:

```python
expected = []
```

Because I compare directly while generating the sorted order.

---

## 3. I had to understand the `i + 1` part

Since heights start from `1`, but indexes start from `0`:

```text
count[0] represents height 1
count[1] represents height 2
count[2] represents height 3
```

That is why we use:

```python
i + 1
```

---

## 4. I confused the original index with the count index

There are two different indexes:

```python
i
```

This goes through the count array.

```python
original_index
```

This goes through the original `heights` array.

They are not the same thing.

---

# What I learned

## 1. Counting sort is useful when the value range is small

Here, heights are only from `1` to `100`.

That makes counting sort a good choice.

---

## 2. We can generate a sorted array without actually sorting

The count array already tells us the sorted order.

Example:

```text
1 appears 3 times
2 appears 1 time
3 appears 1 time
```

So sorted order is:

```text
1, 1, 1, 2, 3
```

---

## 3. We do not always need to store intermediate results

At first, I built:

```python
expected
```

Then compared.

Later, I improved it by comparing directly.

This reduced space from:

```text
O(n)
```

to:

```text
O(1)
```

---

# Pattern

This problem uses the:

```text
Counting Sort / Frequency Array pattern
```

Use this pattern when:

```text
1. The values are integers
2. The range of values is small
3. We need sorted order or frequency information
```

Examples of similar ideas:

```text
- Counting frequencies
- Rebuilding sorted order
- Finding duplicates
- Sorting numbers with small range
- Comparing original array with sorted order
```

---

# Key takeaway

The main trick is:

```python
count[i] = how many times height i + 1 appears
```

Then the sorted order is generated by:

```python
for i in range(100):
    for _ in range(count[i]):
        expected_height = i + 1
```

From there, we can either:

```text
1. Add expected_height to expected array
2. Or compare expected_height directly with heights[original_index]
```

The second option is more space efficient.

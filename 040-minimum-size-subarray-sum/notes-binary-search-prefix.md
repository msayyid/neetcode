# Minimum Size Subarray Sum - Prefix Sum + Binary Search

## Goal of this approach

We want an `O(n log n)` solution.

Instead of:

* trying every subarray by extending step by step

we do this:

* for each starting index, use **prefix sums** to turn the subarray sum into a formula
* then use **binary search** to quickly find the earliest valid ending point

---

# Why this approach works

This approach works because all numbers in `nums` are **positive**.

That means:

* each new prefix sum is larger than the previous one
* so the prefix sum array is **sorted increasing**
* and once something is sorted, we can use **binary search**

Important:

* positive means strictly greater than 0
* `0` is not included

---

# Step 1: Build the prefix sum array

We create an array `prefixSum` of size `n + 1`.

Example:

```python
nums = [2,1,5,1,5,3]
```

Then:

```python
prefixSum = [0,2,3,8,9,14,17]
```

---

## What does `prefixSum[i]` mean?

`prefixSum[i]` means:

> the sum of the first `i` elements

So:

* `prefixSum[0] = 0`
* `prefixSum[1] = 2`
* `prefixSum[2] = 3`
* `prefixSum[3] = 8`

and so on.

### Important indexing detail

`prefixSum[i]` does **not** mean sum up to index `i`.

It means:

> sum of elements from index `0` to index `i - 1`

That is why prefix sums feel confusing at first.

---

## How to build it

```python
prefixSum = [0] * (n + 1)
for i in range(n):
    prefixSum[i + 1] = prefixSum[i] + nums[i]
```

### Why `i + 1`?

Because:

* `prefixSum[0]` is reserved for `0`
* so the sum after seeing `nums[0]` goes into `prefixSum[1]`

---

# Step 2: How prefix sums give subarray sums

If we want the sum from index `i` to index `j`, we use:

```python
prefixSum[j + 1] - prefixSum[i]
```

---

## Why?

Because:

* `prefixSum[j + 1]` = sum from start up to index `j`
* `prefixSum[i]` = sum from start up to index `i - 1`

So subtracting removes everything before `i`.

---

## Example

```python
nums = [2,1,5,1,5,3]
prefixSum = [0,2,3,8,9,14,17]
```

Want sum from index `2` to `4`:

Subarray:

```python
[5,1,5]
```

Formula:

```python
prefixSum[5] - prefixSum[2] = 14 - 3 = 11
```

Correct.

---

# Step 3: What are we searching for?

For each starting index `i`, we want the **smallest ending index `j`** such that:

```python
sum(nums[i...j]) >= target
```

Using prefix sum:

```python
prefixSum[j + 1] - prefixSum[i] >= target
```

Rearrange:

```python
prefixSum[j + 1] >= prefixSum[i] + target
```

This is the key transformation.

---

# Step 4: Main binary search idea

For each starting index `i`:

1. compute how much total we need:

   ```python
   need = prefixSum[i] + target
   ```

2. find the **first position** in `prefixSum` that is:

   ```python
   >= need
   ```

That first position tells us the earliest place where the subarray starting at `i` becomes valid.

---

# Step 5: Why binary search works

Because `prefixSum` is sorted increasing.

Example:

```python
prefixSum = [0,2,3,8,9,14,17]
```

If we need `13`, we want the first value that is at least `13`.

That is `14`.

Instead of scanning one by one, binary search finds it in `O(log n)`.

---

# Binary search target

We are searching for the **first valid end**.

This is a classic:

> find the first index where condition becomes true

The condition is:

```python
curSum >= target
```

or equivalently:

```python
prefixSum[mid + 1] - prefixSum[i] >= target
```

---

# Code structure

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        res = float("inf")

        for i in range(n):
            l, r = i, n
            while l < r:
                mid = (l + r) // 2
                curSum = prefixSum[mid + 1] - prefixSum[i]

                if curSum >= target:
                    r = mid
                else:
                    l = mid + 1

            if l != n and prefixSum[l + 1] - prefixSum[i] >= target:
                res = min(res, l - i + 1)

        return 0 if res == float("inf") else res
```

---

# What the binary search part is doing

```python
l, r = i, n
while l < r:
    mid = (l + r) // 2
    curSum = prefixSum[mid + 1] - prefixSum[i]

    if curSum >= target:
        r = mid
    else:
        l = mid + 1
```

This means:

> among all possible ending indices from `i` to `n - 1`, find the first one whose subarray sum is at least target

---

# Step-by-step meaning of each part

## `l, r = i, n`

We search only ending positions that are valid for this start.

* `i` is the earliest possible ending index
* `n` is used as the upper boundary

---

## `mid = (l + r) // 2`

Standard binary search midpoint.

---

## `curSum = prefixSum[mid + 1] - prefixSum[i]`

This calculates:

> sum of subarray from `i` to `mid`

This was one of your biggest confusion points.

### Why `mid + 1`?

Because:

* `prefixSum[k]` stores sum of first `k` elements
* to include index `mid`, we need the sum up to `mid`
* that is stored at `prefixSum[mid + 1]`

---

## `if curSum >= target`

This means:

> subarray from `i` to `mid` is valid

So `mid` could be an answer.

But maybe there is an even smaller valid end index.

So we move left:

```python
r = mid
```

---

## `else: l = mid + 1`

This means:

> subarray is too small, need a larger end index

So move right.

---

# The pattern binary search is finding

For a fixed `i`, the possible end indices often look like this:

```python
False False False True True True
```

Meaning:

* too small
* too small
* too small
* valid
* valid
* valid

Binary search is finding the **first True**.

That first True is the smallest valid ending index.

---

# Full intuition in one sentence

For each starting index `i`, we binary search for the earliest ending index `j` such that the sum from `i` to `j` is at least `target`.

---

# How to compute the length

Once binary search finishes:

```python
length = l - i + 1
```

Because:

* start index = `i`
* end index = `l`

So number of elements is:

```python
l - i + 1
```

---

# Why do we check `l != n`?

If binary search ends with:

```python
l == n
```

that means:

> no valid ending index was found

So we should not update the answer.

---

# Complexity

## Time

* building prefix sum: `O(n)`
* looping through each start index: `O(n)`
* binary search for each start: `O(log n)`

Total:

```python
O(n log n)
```

---

## Space

* prefix sum array of size `n + 1`

So:

```python
O(n)
```

---

# Your main struggles and mistakes

## 1. Prefix sum indexing confusion

This was your biggest issue.

You were confused about:

```python
prefixSum[mid + 1] - prefixSum[i]
```

### Correct understanding

* `prefixSum[k]` = sum of first `k` elements
* so to include `mid`, use `mid + 1`

This is the shifted indexing part that makes prefix sums feel weird.

---

## 2. Not understanding what binary search was searching for

At first, it looked like random pointer movement.

But the real question is:

> for this start index `i`, what is the first end index `j` where the sum becomes big enough?

That is what binary search is solving.

---

## 3. Thinking it might be O(n²)

You thought:

> if we loop outside and search inside, isn’t that O(n²)?

That would be true if the inside part were a linear scan.

But it is not.

It is **binary search**, so the inside part is `O(log n)`, not `O(n)`.

That is why total is:

```python
O(n log n)
```

not `O(n²)`.

---

## 4. Trouble building the prefix sum array

You first wrote a version that did not accumulate properly.

Correct logic is:

```python
prefixSum[i + 1] = prefixSum[i] + nums[i]
```

Each new prefix builds on the previous one.

---

## 5. Return trick confusion

You saw this:

```python
return res % (n + 1)
```

That works only as a shortcut trick when `res` starts as `n + 1`.

It is not clear.

Better:

```python
return 0 if res == float("inf") else res
```

Much clearer.

---

# Clean interview explanation

> I build a prefix sum array so I can compute any subarray sum in O(1). For each starting index, I binary search for the earliest ending index where the subarray sum reaches the target. Since the prefix sum array is strictly increasing because all numbers are positive, binary search is valid. This gives an O(n log n) solution.

---

# Final short revision version

## Prefix sum

* `prefixSum[i]` = sum of first `i` elements
* build with:

  ```python
  prefixSum[i + 1] = prefixSum[i] + nums[i]
  ```

## Subarray sum

* sum from `i` to `j`:

  ```python
  prefixSum[j + 1] - prefixSum[i]
  ```

## Binary search idea

* for each `i`, find smallest `j` such that:

  ```python
  prefixSum[j + 1] - prefixSum[i] >= target
  ```

## Binary search rule

* if current sum is valid → go left
* if current sum is too small → go right

## Complexity

* Time: `O(n log n)`
* Space: `O(n)`

## Biggest things to remember

* prefix uses shifted indexing
* `mid + 1` is needed to include `mid`
* binary search finds the first valid end index
* this works only because prefix sums are increasing


----
----
____


Here is the **short exam / interview revision version**:

---

# Minimum Size Subarray Sum - Prefix + Binary Search (Quick Notes)

## Core Idea

* Use **prefix sum** to get subarray sums in O(1)
* For each start index `i`, **binary search** the smallest end index `j` such that sum ≥ target

---

## Prefix Sum

```python
prefix[0] = 0
prefix[i+1] = prefix[i] + nums[i]
```

Meaning:

```text
prefix[k] = sum of first k elements (nums[0..k-1])
```

---

## Subarray Sum Formula

```python
sum(i → j) = prefix[j + 1] - prefix[i]
```

---

## Binary Search Goal

For each `i`, find smallest `j` such that:

```python
prefix[j + 1] - prefix[i] >= target
```

Equivalent:

```python
prefix[j + 1] >= prefix[i] + target
```

---

## Binary Search Logic

```python
l, r = i, n
while l < r:
    mid = (l + r) // 2
    curSum = prefix[mid + 1] - prefix[i]

    if curSum >= target:
        r = mid      # try smaller j
    else:
        l = mid + 1  # need bigger j
```

---

## Key Pattern

Binary search finds:

```text
False False False True True True
             ↑
        first valid j
```

---

## Length

```python
length = j - i + 1
```

---

## Edge Case

```python
if j == n → no valid subarray
```

---

## Complexity

* Time: `O(n log n)`
* Space: `O(n)`

---

## Must Remember

* prefix uses **shifted indexing**
* use `mid + 1` to include `mid`
* binary search finds **first valid end**
* works only because numbers are **positive → prefix sorted**

---

## One-liner intuition

> For each start, jump to the earliest valid end using binary search instead of building the sum step by step.

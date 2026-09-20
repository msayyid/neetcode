# 912. Sort an Array

---

# Approach 1 — Simple Brute-Force Swapping

This is the first working version you came up with.

```python
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        # Go through every position in the array
        for i in range(len(nums)):

            # Compare nums[i] with everything from i onward
            for j in range(i, len(nums)):

                # If we find a smaller value,
                # immediately swap it into position i
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums
```

### Idea

For every index `i`, you look through the remaining part of the array:

```text
[5, 2, 4, 1]
 ^
 i
```

If you find something smaller than `nums[i]`, you immediately swap it.

For example:

```text
[5, 2, 4, 1]

5 > 2
→ swap

[2, 5, 4, 1]

2 > 1
→ swap

[1, 5, 4, 2]
```

Then move to the next `i`.

This eventually sorts the array, but it may perform **many swaps during one pass**.

### Important distinction

This is not exactly standard selection sort.

It is more like a simple **exchange-sort style** solution:

> Find something smaller → immediately swap.

Selection sort instead remembers the smallest value and performs only **one swap per outer iteration**.

### Complexity

The loops still perform roughly:

```text
n + (n-1) + (n-2) + ... + 1
```

comparisons.

Therefore:

| Case    |    Time |
| ------- | ------: |
| Best    | `O(n²)` |
| Average | `O(n²)` |
| Worst   | `O(n²)` |

Even if the array is already sorted, the nested loops still run.

Extra space:

```text
O(1)
```

because everything is done in place.

### Memory line

> Compare the current value with everything after it and swap immediately whenever a smaller value is found.

---

# Approach 2 — Selection Sort

This is the proper selection sort you wrote.

```python
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        # i represents the position where
        # the next smallest value should be placed
        for i in range(len(nums)):

            # Assume nums[i] is the smallest value
            # in the remaining unsorted part
            min_index = i

            # Search the rest of the array
            # for an even smaller value
            for j in range(i + 1, len(nums)):

                if nums[j] < nums[min_index]:
                    # Remember the index of the
                    # smallest value found so far
                    min_index = j

            # Put the smallest remaining value at index i
            #
            # If min_index == i, this just swaps
            # the element with itself, which is harmless
            nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums
```

### Core idea

Selection sort divides the array conceptually into:

```text
[ sorted part | unsorted part ]
```

At each step:

1. Search the unsorted part.
2. Find the smallest value.
3. Put it at the beginning of the unsorted part.
4. Grow the sorted part by one.

Example:

```text
[5, 2, 4, 1]
```

First pass:

```text
smallest = 1

[1, 2, 4, 5]
 ^
 sorted
```

Second pass:

Search:

```text
[2, 4, 5]
```

smallest is already `2`.

So nothing meaningful changes.

Then continue.

### Why `min_index` matters

We start:

```python
min_index = i
```

meaning:

> "For now, assume the current value is the smallest."

Then:

```python
if nums[j] < nums[min_index]:
    min_index = j
```

means:

> "I found something smaller. Remember where it is."

We don't swap immediately.

Only after the whole remaining section has been searched do we swap:

```python
nums[i], nums[min_index] = nums[min_index], nums[i]
```

That's the major difference from Approach 1.

### Complexity

Selection sort always scans the unsorted portion completely.

So:

| Case    |    Time |
| ------- | ------: |
| Best    | `O(n²)` |
| Average | `O(n²)` |
| Worst   | `O(n²)` |

Even:

```text
[1, 2, 3, 4, 5]
```

still causes all those comparisons.

Space:

```text
O(1)
```

because sorting happens directly inside `nums`.

### One advantage over Approach 1

Selection sort performs at most roughly:

```text
O(n)
```

swaps.

Approach 1 can perform many more swaps.

But both still have:

```text
O(n²)
```

time complexity.

### Memory line

> Find the smallest value in the unsorted part, then move it to the front of that part.

---

# Approach 3 — Heap Sort

This is the approach that actually satisfies LeetCode 912's requirement:

```text
O(n log n) time
small extra space
```

We use a **max heap**.

```python
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        def heapify(i, heap_size):
            """
            Fix the subtree starting at index i
            so that it follows the max-heap rule:

            parent >= children
            """

            while True:
                # For now, assume the parent is the largest
                largest = i

                # Find the indexes of its children
                left = 2 * i + 1
                right = 2 * i + 2

                # If the left child exists and is bigger
                # than our current largest, remember it
                if left < heap_size and nums[left] > nums[largest]:
                    largest = left

                # Check the right child as well
                if right < heap_size and nums[right] > nums[largest]:
                    largest = right

                # If the parent is already the largest,
                # this part of the heap is valid
                if largest == i:
                    break

                # Otherwise swap the parent with
                # its larger child
                nums[i], nums[largest] = nums[largest], nums[i]

                # The old parent was pushed downward.
                # Continue heapifying from its new position.
                i = largest

        # ---------------------------------------
        # STEP 1: Build the max heap
        # ---------------------------------------

        # n // 2 - 1 is the last parent node.
        #
        # Move backward from the last parent to index 0,
        # heapifying every parent.
        for i in range(n // 2 - 1, -1, -1):
            heapify(i, n)

        # ---------------------------------------
        # STEP 2: Sort using the max heap
        # ---------------------------------------

        # nums[0] is now always the largest value
        # in the active heap.
        #
        # Move that largest value to the end,
        # shrink the heap, and restore the heap again.
        for end in range(n - 1, 0, -1):

            # Move the current largest value
            # into its final sorted position
            nums[0], nums[end] = nums[end], nums[0]

            # Restore the heap, but only for indexes
            # 0 ... end - 1.
            #
            # nums[end:] is already sorted and
            # should no longer be touched.
            heapify(0, end)

        return nums
```

---

## Understanding Heap Sort

There are really only **two big stages**.

## Stage 1 — Build a max heap

Suppose:

```text
nums = [4, 10, 3, 5, 1]
```

An array can represent a binary tree.

For index `i`:

```python
left = 2 * i + 1
right = 2 * i + 2
```

So:

```text
        4
      /   \
    10     3
   /  \
  5    1
```

A max heap requires:

```text
parent >= children
```

We start at the last parent:

```python
n // 2 - 1
```

For `n = 5`:

```text
5 // 2 - 1
= 1
```

So:

```python
range(1, -1, -1)
```

produces:

```text
1, 0
```

We heapify index `1`, then index `0`.

Eventually:

```text
[4, 10, 3, 5, 1]
```

becomes:

```text
[10, 5, 3, 4, 1]
```

which represents:

```text
       10
      /  \
     5    3
    / \
   4   1
```

Now the largest element is guaranteed to be:

```python
nums[0]
```

---

# What `heapify()` actually does

Suppose we have:

```text
[4, 10, 3, 5, 1]
```

and call:

```python
heapify(0, 5)
```

Start:

```text
i = 0
largest = 0
```

Children:

```text
left  = 1 → value 10
right = 2 → value 3
```

`10` is largest, so:

```text
largest = 1
```

Swap:

```text
[4, 10, 3, 5, 1]
→
[10, 4, 3, 5, 1]
```

Now the old parent `4` was pushed to index `1`.

That's why:

```python
i = largest
```

makes:

```text
i = 1
```

We're basically saying:

> Follow the old parent downward and make sure it is valid there too.

Now:

```text
parent = 4
children = 5 and 1
```

`5 > 4`, so:

```text
[10, 4, 3, 5, 1]
→
[10, 5, 3, 4, 1]
```

Then `4` moves to index `3`.

Index `3` has no children.

So:

```python
largest == i
```

and heapify stops.

---

# Stage 2 — Move the maximum to the end

Once we have:

```text
[10, 5, 3, 4, 1]
```

we know:

```text
10 = largest
```

Swap it with the last element:

```text
[10, 5, 3, 4, 1]
→
[1, 5, 3, 4, 10]
```

Now:

```text
10
```

is in its final sorted position.

So we tell heapify:

```python
heapify(0, 4)
```

Notice `4`, not `5`.

That means:

> Only indexes `0, 1, 2, 3` belong to the heap now. Ignore index `4`.

So:

```text
[1, 5, 3, 4 | 10]
                 ^
              sorted
```

Heapify produces:

```text
[5, 4, 3, 1 | 10]
```

Then move `5` to its final place:

```text
[1, 4, 3 | 5, 10]
```

Heapify:

```text
[4, 1, 3 | 5, 10]
```

Then:

```text
[3, 1 | 4, 5, 10]
```

Then finally:

```text
[1, 3, 4, 5, 10]
```

---

# Why heapify does NOT sort the heap

This is important.

If the active heap is:

```text
[4, 1, 3]
```

that is already a valid max heap:

```text
    4
   / \
  1   3
```

It is not completely sorted:

```text
4, 1, 3
```

but that's okay.

Heapify only guarantees:

```text
parent >= children
```

The **outer sorting loop** is what gradually produces the sorted array.

---

# Heap Sort Complexity

## Building the heap

The build phase:

```python
for i in range(n // 2 - 1, -1, -1):
```

is actually:

```text
O(n)
```

This is a special property of heap construction.

## Sorting phase

We perform roughly `n` extractions:

```text
n times
```

and every heapify can move down the tree by about:

```text
log n
```

levels.

Therefore:

```text
O(n log n)
```

overall.

### Heap Sort Complexity Table

| Case    |         Time |
| ------- | -----------: |
| Best    | `O(n log n)` |
| Average | `O(n log n)` |
| Worst   | `O(n log n)` |

Extra space with our **iterative heapify**:

```text
O(1)
```

because we're only storing variables like:

```text
i
largest
left
right
end
```

and modifying `nums` directly.

---

# Final Comparison

| Approach        |         Best |      Average |        Worst | Extra Space |
| --------------- | -----------: | -----------: | -----------: | ----------: |
| Simple swapping |      `O(n²)` |      `O(n²)` |      `O(n²)` |      `O(1)` |
| Selection Sort  |      `O(n²)` |      `O(n²)` |      `O(n²)` |      `O(1)` |
| Heap Sort       | `O(n log n)` | `O(n log n)` | `O(n log n)` |      `O(1)` |

For **LeetCode 912**, heap sort is the one of these three that satisfies:

```text
O(n log n) time
+
smallest auxiliary space
```

The progression we went through is useful to remember as:

```text
Approach 1
"See smaller → swap immediately"
        ↓

Selection Sort
"Find smallest → swap once"
        ↓

Heap Sort
"Keep largest efficiently available using a heap,
move it to the end repeatedly"
```

And the shortest heap-sort memory line I'd keep is:

> **Build max heap → swap root with end → shrink heap → heapify root → repeat.**

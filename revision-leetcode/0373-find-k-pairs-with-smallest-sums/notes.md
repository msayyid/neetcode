# 373. Find K Pairs with Smallest Sums - Revision Notes

## 1. Problem Summary

You are given two sorted arrays:

```python
nums1
nums2
```

You need to return the `k` pairs `[u, v]` with the smallest sums, where:

```python
u comes from nums1
v comes from nums2
```

Example:

```python
nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
```

All possible pairs:

```text
[1,2] = 3
[1,4] = 5
[1,6] = 7
[7,2] = 9
...
```

Answer:

```python
[[1,2], [1,4], [1,6]]
```

Key constraint:

```text
nums1.length, nums2.length <= 100000
k <= 10000
```

So generating all pairs is too expensive.

---

# 2. My Initial Understanding

Your first idea was brute force:

```python
for n1 in nums1:
    for n2 in nums2:
        store pair sum
```

Then sort or heap-pop the smallest `k`.

This shows you understood the basic requirement correctly:

* Every answer is a pair from `nums1` and `nums2`
* The pair is ranked by `n1 + n2`
* We need the first `k` smallest sums

The confusion started when trying to avoid generating all pairs.

You were unsure why, after popping `(i, j)`, we push `(i, j + 1)` instead of maybe `(i + 1, j)`.

That was the main conceptual gap.

---

# 3. Mistakes I Made

## Mistake 1: Generating all possible pairs

Your first brute force version did this:

```python
for n1 in nums1:
    for n2 in nums2:
        result.append([n1 + n2, n1, n2])
```

This is correct logically, but not efficient.

Why it fails:

```text
If nums1 has 100000 elements and nums2 has 100000 elements,
total pairs = 100000 * 100000 = 10^10
```

That is too much memory.

Complexity:

```text
Time:  O(n * m * log(n * m))
Space: O(n * m)
```

This causes Memory Limit Exceeded.

---

## Mistake 2: Using a heap but still pushing all pairs

You then changed the code to use a heap:

```python
for i in range(len(nums1)):
    for j in range(len(nums2)):
        heapq.heappush(pairs, (nums1[i] + nums2[j], nums1[i], nums2[j]))
```

This still has the same problem.

Even though you used a heap, you still generated all `n * m` pairs.

So it is still brute force.

Complexity:

```text
Time:  O(n * m * log(n * m))
Space: O(n * m)
```

Using a heap does not automatically make it optimized. The important part is how many items you put into the heap.

---

## Mistake 3: Thinking `(i, j + 1)` must be the next global smallest

You were worried:

> Why do we push `(i, j + 1)`? What if `(i + 1, j)` is smaller?

This was a good question.

The answer:

```text
(i, j + 1) is not guaranteed to be the next smallest overall.
It is only the next smallest pair from the same row.
```

The heap decides the true global smallest.

So we are not manually choosing the next answer. We are only revealing the next candidate from one row.

---

# 4. Things I Learned

## Key idea: Treat pairs as a matrix

Because both arrays are sorted, we can imagine all pair sums as a matrix.

Example:

```python
nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
```

Matrix of pairs:

```text
             nums2[0]   nums2[1]   nums2[2]
             2          4          6

nums1[0] 1   (1,2)=3    (1,4)=5    (1,6)=7
nums1[1] 7   (7,2)=9    (7,4)=11   (7,6)=13
nums1[2] 11  (11,2)=13  (11,4)=15  (11,6)=17
```

Each row is sorted left to right because `nums2` is sorted.

For a fixed `nums1[i]`:

```text
nums1[i] + nums2[0]
nums1[i] + nums2[1]
nums1[i] + nums2[2]
```

The sums only increase as `j` moves right.

---

## Key observation

The first pair of each row is the smallest pair in that row.

So instead of pushing every pair, push only:

```text
(i, 0)
```

for each row.

That means:

```text
(nums1[0], nums2[0])
(nums1[1], nums2[0])
(nums1[2], nums2[0])
...
```

Then whenever we pop `(i, j)`, we reveal the next pair from the same row:

```text
(i, j + 1)
```

---

## Why `j + 1 < len(nums2)` matters

This check:

```python
if j + 1 < len(nums2):
```

means:

```text
Does this row still have another pair?
```

If yes, push the next column.

If no, the row is finished.

Example:

```text
row: (1,2), (1,4), (1,6)
```

If we popped `(1,6)`, there is no next pair in that row.

So we push nothing.

---

## Why `min(len(nums1), k)` works

Initial heap setup:

```python
for i in range(min(len(nums1), k)):
```

We do not need to start with more than `k` rows because the answer only needs `k` pairs.

If `k = 3`, there is no point initially pushing 100000 rows.

Heap size should stay small.

More precise heap size:

```text
h = min(len(nums1), k)
```

---

# 5. Pattern Recognition

## Main Pattern

```text
Min Heap + Sorted Matrix / Merge K Sorted Lists
```

## Trigger: How to recognize this pattern

Think of this pattern when:

* You need the `k` smallest or `k` largest combinations
* Input arrays are already sorted
* Brute force creates too many combinations
* Each row/list has an internal sorted order
* You can reveal the next candidate only after taking the current one

The important clue here is:

```text
nums1 and nums2 are sorted.
```

That means pair sums form sorted rows.

So instead of generating all combinations, we use a heap to merge sorted rows.

---

## Why this pattern applies here

Each row behaves like a sorted list:

```text
Row 0: nums1[0] + nums2[0], nums1[0] + nums2[1], nums1[0] + nums2[2]
Row 1: nums1[1] + nums2[0], nums1[1] + nums2[1], nums1[1] + nums2[2]
Row 2: nums1[2] + nums2[0], nums1[2] + nums2[1], nums1[2] + nums2[2]
```

So the problem becomes:

```text
Find k smallest values from multiple sorted lists.
```

That is a heap problem.

---

## Similar problem types

This pattern appears in:

* K-way merge
* Merge k sorted lists
* Kth smallest element in a sorted matrix
* K smallest pair sums
* Top k combinations from sorted arrays
* Problems where you need to avoid generating all combinations

---

# 6. Approaches Tried

## Approach 1: Brute Force + Sort

### Main idea

Generate every possible pair, sort by sum, return first `k`.

### Algorithm

1. Create an empty list.
2. Loop through every `n1` in `nums1`.
3. Loop through every `n2` in `nums2`.
4. Store `[sum, n1, n2]`.
5. Sort by sum.
6. Return first `k` pairs.

### Pseudocode

```text
pairs = []

for n1 in nums1:
    for n2 in nums2:
        pairs.append([n1 + n2, n1, n2])

sort pairs by sum

answer = first k pairs without the sum
return answer
```

### Time complexity

```text
O(n * m * log(n * m))
```

### Space complexity

```text
O(n * m)
```

### Why it works

It checks every possible pair, so it cannot miss the smallest pairs.

### Limitation

It stores too many pairs.

Fails for large constraints.

### Interview expected?

No.

This is a valid starting brute force approach, but not interview-expected as the final answer.

---

## Approach 2: Brute Force + Heap

### Main idea

Generate every possible pair and push it into a min heap.

Then pop `k` times.

### Algorithm

1. Create a min heap.
2. Push every pair into the heap with its sum.
3. Pop the smallest pair `k` times.

### Pseudocode

```text
heap = []

for i in range(len(nums1)):
    for j in range(len(nums2)):
        push (nums1[i] + nums2[j], nums1[i], nums2[j])

answer = []

repeat k times:
    pop smallest pair
    add to answer

return answer
```

### Time complexity

```text
O(n * m * log(n * m))
```

### Space complexity

```text
O(n * m)
```

### Why it works

The heap always pops the smallest sum first.

### Limitation

Still stores all pairs.

So it can still cause Memory Limit Exceeded.

### Interview expected?

No.

It is similar to brute force. The heap alone does not fix the problem.

---

## Approach 3: Optimized Min Heap Using Sorted Rows

### Main idea

Do not generate all pairs.

Treat all pairs as a matrix.

Each row is sorted, so initially push only the first pair from each row.

When a pair `(i, j)` is popped, push `(i, j + 1)` from the same row.

### Algorithm

1. Create a min heap.
2. Push `(nums1[i] + nums2[0], i, 0)` for `i` from `0` to `min(len(nums1), k) - 1`.
3. Repeat `k` times:

   * Pop the smallest pair from the heap.
   * Add `[nums1[i], nums2[j]]` to result.
   * If `j + 1` exists, push `(nums1[i] + nums2[j + 1], i, j + 1)`.
4. Return result.

### Pseudocode

```text
heap = []

for i in range(min(len(nums1), k)):
    push (nums1[i] + nums2[0], i, 0)

answer = []

repeat k times:
    sum, i, j = pop heap
    answer.append([nums1[i], nums2[j]])

    if j + 1 < len(nums2):
        push (nums1[i] + nums2[j + 1], i, j + 1)

return answer
```

### Time complexity

Let:

```text
h = min(len(nums1), k)
```

Initial heap filling:

```text
O(h log h)
```

Main loop:

```text
O(k log h)
```

Overall:

```text
O(k log min(k, len(nums1)))
```

Usually simplified as:

```text
O(k log k)
```

### Space complexity

Heap stores at most `min(k, len(nums1))` elements.

Result stores `k` pairs.

```text
O(k)
```

### Why it works

The heap always stores the next best available pair from each row.

Since every row is sorted, we only need to reveal the next pair in a row after the previous pair from that row has been used.

The heap compares candidates from all rows and gives the global smallest.

### Interview expected?

Yes.

This is the expected optimized solution.

---

# 7. Optimized Approach Explained Simply

The optimized solution avoids this:

```text
Generate all pairs first.
```

Instead, it does this:

```text
Generate pairs only when they become possible candidates.
```

At the beginning, every row's best pair is at column `0`.

So we push:

```text
(i, 0)
```

for each row.

When we pop `(i, j)`, we have used that pair.

The next pair in the same row is:

```text
(i, j + 1)
```

So we push that.

Important:

```text
We do not know if (i, j + 1) is the next answer.
The heap decides that.
```

We only make it available as a candidate.

---

# 8. Final Code

You asked for notes, so I will not include full final code here.

Your final code structure is correct.

Cleaner standard version would mainly use tuples instead of lists in the heap:

```python
(nums1[i] + nums2[0], i, 0)
```

instead of:

```python
[nums1[i] + nums2[0], i, 0]
```

Both work in Python, but tuples are more standard for heap entries.

---

# 9. Interview Script

You can explain it like this:

```text
The brute force approach is to generate all possible pairs from nums1 and nums2, sort them by sum, and return the first k pairs. This works logically, but it is too expensive because there can be n * m pairs, which is impossible to store for large constraints.

The key observation is that both arrays are sorted. If I imagine all pair sums as a matrix, each row fixes one element from nums1 and pairs it with every element from nums2. Since nums2 is sorted, each row is sorted from left to right.

So this becomes similar to merging multiple sorted lists. I use a min heap to store only the smallest currently available pair from each row.

Initially, I push the first pair from each row: nums1[i] with nums2[0]. I only push up to min(len(nums1), k) rows because I only need k results.

Then I repeat k times. I pop the smallest pair from the heap and add it to the answer. If the popped pair was at indices (i, j), then the next pair from the same row is (i, j + 1), so I push that if it exists.

The heap always chooses the smallest available candidate globally, while I only reveal the next candidate from a row when needed.

The time complexity is O(k log min(k, len(nums1))) and the space complexity is O(k).
```

---

# 10. Edge Cases and Dry Run

## Edge Case 1: `nums2` has one element

```python
nums1 = [1, 2, 3]
nums2 = [10]
k = 2
```

Initial heap:

```text
(1,10)
(2,10)
```

Pop `(1,10)`.

`j + 1 < len(nums2)` becomes:

```text
1 < 1
```

False.

So we push nothing.

Then pop `(2,10)`.

Works correctly.

---

## Edge Case 2: `nums1` has one element

```python
nums1 = [1]
nums2 = [2, 4, 6]
k = 3
```

Initial heap:

```text
(1,2)
```

Pop `(1,2)`, push `(1,4)`.

Pop `(1,4)`, push `(1,6)`.

Pop `(1,6)`, push nothing.

Answer:

```python
[[1,2], [1,4], [1,6]]
```

Works correctly.

---

## Edge Case 3: Duplicates

```python
nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
k = 2
```

Duplicate pairs are allowed because they come from different indices.

Answer can be:

```python
[[1,1], [1,1]]
```

No special handling needed.

---

## Dry Run

```python
nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
```

Initial heap:

```text
(1+2=3, i=0, j=0)
(7+2=9, i=1, j=0)
(11+2=13, i=2, j=0)
```

Pop:

```text
(1,2)
```

Add to result:

```python
[[1,2]]
```

Push next from same row:

```text
(1,4)
```

Heap:

```text
(1,4)=5
(7,2)=9
(11,2)=13
```

Pop:

```text
(1,4)
```

Result:

```python
[[1,2], [1,4]]
```

Push:

```text
(1,6)
```

Heap:

```text
(1,6)=7
(7,2)=9
(11,2)=13
```

Pop:

```text
(1,6)
```

Result:

```python
[[1,2], [1,4], [1,6]]
```

Stop because we have `k = 3`.

---

# 11. Key Takeaways

```text
Do not generate all pairs.
```

The sorted arrays create a sorted matrix of pair sums.

Each row is sorted left to right.

Use a min heap to store only the next available pair from each row.

After popping `(i, j)`, push `(i, j + 1)`.

The heap decides the global smallest.

`min(len(nums1), k)` keeps the heap small.

`j + 1 < len(nums2)` prevents going past the row.

Final complexity:

```text
Time:  O(k log min(k, len(nums1)))
Space: O(k)
```

Interview expected:

```text
Yes, this is the expected optimized solution.
```

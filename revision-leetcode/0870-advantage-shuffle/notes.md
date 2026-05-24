# LeetCode 870 - Advantage Shuffle Notes

## 1. Problem Summary

You are given two arrays:

```python
nums1
nums2
```

Both have the same length.

You can reorder `nums1` in any way. Your goal is to return a permutation of `nums1` that maximizes the number of indices where:

```python
nums1[i] > nums2[i]
```

This count is called the **advantage**.

Important point:

You are not trying to make every value in `nums1` bigger than every parallel value in `nums2`.

You are trying to maximize how many positions are wins.

## 2. My Initial Understanding

At first, you thought the goal was to arrange `nums1` so that all elements become bigger than the matching elements in `nums2`.

That understanding was not fully correct.

The correct goal is:

```python
maximize the number of winning positions
```

Each index is counted as either:

```python
win = 1
loss_or_tie = 0
```

Winning by a lot does not matter. A win by `+1` and a win by `+100` both count as one win.

You also considered subtracting:

```python
nums1[i] - nums2[i]
```

and maximizing the total sum. But that does not work because the total sum stays the same no matter how `nums1` is reordered:

```python
sum(nums1) - sum(nums2)
```

does not change.

## 3. Mistakes I Made

### Mistake 1: Thinking we maximize total difference

You thought maybe the problem wants the permutation with the maximum total difference.

But this is wrong because the total difference is always fixed.

Example:

```python
nums1 = [100, 2]
nums2 = [50, 1]
```

Permutation 1:

```python
[100, 2]
```

Wins:

```python
100 > 50  # win
2 > 1     # win
```

Advantage = `2`

Permutation 2:

```python
[2, 100]
```

Wins:

```python
2 > 50    # lose
100 > 1   # win
```

Advantage = `1`

But both have the same total difference. So sum difference is not useful.

### Mistake 2: Mapping sorted nums2 values directly to sorted nums1 values

Your first idea was:

```python
nums1.sort()
nums2_sorted = sorted(nums2)

for i in range(len(nums1)):
    the_map[nums2_sorted[i]] = nums1[i]
```

This pairs the smallest `nums1` with the smallest `nums2`, second smallest with second smallest, and so on.

But this does not check whether the pairing actually gives a win.

Example:

```python
nums1 = [8, 12, 24, 32]
nums2 = [11, 13, 25, 32]
```

Sorted-to-sorted pairing gives:

```python
8  vs 11   # lose
12 vs 13   # lose
24 vs 25   # lose
32 vs 32   # lose
```

So it can miss better pairings.

### Mistake 3: Using a dictionary with nums2 values

A dictionary like this can break when `nums2` has duplicates:

```python
the_map[nums2_sorted[i]] = nums1[i]
```

Example:

```python
nums2 = [5, 5, 5]
```

A dictionary can only have one key `5`, so previous values get overwritten.

That is why we store:

```python
(nums2 value, original index)
```

instead of only storing the value.

## 4. Things I Learned

### Key idea

Use the smallest possible `nums1` value that can win.

If the smallest remaining `nums1` cannot beat even the smallest remaining `nums2`, then it cannot beat anyone. So we sacrifice it against the largest remaining `nums2`.

### Important observation

If:

```python
smallest nums1 <= smallest nums2
```

then this smallest `nums1` cannot beat any remaining `nums2`, because all remaining `nums2` values are at least as large as the smallest one.

So it is useless for winning and should be sacrificed.

### Why we sort nums2 with indices

We sort `nums2` to process opponents from easiest to hardest, but the final result must match the original order of `nums2`.

So we store pairs:

```python
(value, original_index)
```

Example:

```python
nums2 = [13, 25, 32, 11]
```

Sorted with indices:

```python
[(11, 3), (13, 0), (25, 1), (32, 2)]
```

This tells us where to place the chosen `nums1` value in the result.

## 5. Pattern Recognition

Main pattern:

```text
Greedy + Sorting + Two Pointers
```

### Trigger: How to recognize this pattern

The clue is:

```text
We can reorder one array to maximize the number of pairwise wins.
```

This usually suggests sorting because we want to compare values strategically.

Other signs:

* We need to maximize the number of successful matchups.
* Each value can be used once.
* We want to avoid wasting strong values.
* A local optimal choice is available: use the smallest value that can win.

### Why greedy works here

At every step, we make one of two safe choices:

1. If the smallest `nums1` can beat the smallest `nums2`, use it there.

   * This gives a win as cheaply as possible.

2. If the smallest `nums1` cannot beat the smallest `nums2`, sacrifice it.

   * It cannot beat any remaining `nums2`, so using it against the largest `nums2` loses nothing.

This is why the greedy choice is safe.

### Similar problem types

This pattern appears in problems where you:

* Match items to maximize wins.
* Assign resources to tasks.
* Use the smallest sufficient resource.
* Sacrifice weak items when they cannot help.

Examples of similar ideas:

* Assign Cookies
* Boats to Save People
* Queue-style greedy matching problems
* Scheduling or pairing problems after sorting

## 6. Approaches Tried

## Approach 1: Sorted-to-sorted mapping

### Main idea

Sort both arrays and pair values by position.

### Step-by-step algorithm

1. Sort `nums1`.
2. Sort `nums2`.
3. Map each sorted `nums2` value to the corresponding sorted `nums1` value.
4. Build result using original `nums2`.

### Pseudocode

```python
sort nums1
sort nums2

for i in range(n):
    map[nums2_sorted[i]] = nums1[i]

for i in range(n):
    result[i] = map[nums2[i]]
```

### Time complexity

```text
O(n log n)
```

### Space complexity

```text
O(n)
```

### Why this approach is incomplete

It does not check whether:

```python
nums1[i] > nums2[i]
```

It may pair values in a way that loses too many positions.

Also, dictionary mapping breaks when `nums2` has duplicate values.

### Interview expected?

No. This is a starting idea, but not interview-expected.

## Approach 2: Greedy smallest nums1 first

### Main idea

Sort `nums1`.

Sort `nums2` with original indices.

Always take the smallest remaining `nums1`.

* If it can beat the smallest remaining `nums2`, use it there.
* Otherwise, sacrifice it against the largest remaining `nums2`.

### Step-by-step algorithm

1. Sort `nums1`.
2. Create sorted pairs from `nums2`:

```python
(value, original_index)
```

3. Use one pointer for `nums1`:

   * `left`

4. Use two pointers for sorted `nums2`:

   * `left2` for smallest remaining `nums2`
   * `right2` for largest remaining `nums2`

5. While there are still `nums2` values left:

   * If `nums1[left] > sorted_nums2[left2][0]`, place it at the original index of `sorted_nums2[left2]`.
   * Otherwise, place it at the original index of `sorted_nums2[right2]` as a sacrifice.
   * Move `left` because that `nums1` value has been used.

### Pseudocode

```python
sort nums1
sorted_nums2 = sorted pairs of (value, original_index)

left = 0
left2 = 0
right2 = n - 1

while left2 <= right2:
    if nums1[left] > sorted_nums2[left2].value:
        result[sorted_nums2[left2].index] = nums1[left]
        left2 += 1
    else:
        result[sorted_nums2[right2].index] = nums1[left]
        right2 -= 1

    left += 1
```

### Time complexity

Sorting takes:

```text
O(n log n)
```

Loop takes:

```text
O(n)
```

Total:

```text
O(n log n)
```

### Space complexity

```text
O(n)
```

Because we store sorted `nums2` pairs and the result array.

### Why this approach works

If the smallest remaining `nums1` can beat the smallest remaining `nums2`, that is the cheapest possible win.

If the smallest remaining `nums1` cannot beat the smallest remaining `nums2`, it cannot beat anything remaining. So sacrificing it is safe.

### Interview expected?

Yes. This is interview-expected.

## 7. Optimized Approach

The optimized approach is the greedy sorted approach.

It is better than the initial mapping approach because it actively checks whether a value can win.

Instead of blindly pairing sorted values, it makes a decision:

```python
Can my smallest remaining nums1 win?
```

If yes, take the win.

If no, sacrifice it.

The pattern is:

```text
Greedy + Sorting + Two Pointers
```

Sorting helps us know the easiest and hardest remaining opponents.

The two pointers on `nums2` help us choose whether to place the current `nums1` value against:

```python
smallest nums2  # for a win
```

or:

```python
largest nums2   # for a sacrifice
```

## 8. Final Code

You asked earlier to keep your code unchanged and only add comments, so full code is not repeated here.

Your final code is correct and interview-acceptable.

One small cleanup possible:

```python
sorted_nums2 = [(num, i) for i, num in enumerate(nums2)]
```

instead of:

```python
sorted_nums2 = [(nums2[i], i) for i in range(len(nums2))]
```

But your current version is completely fine.

## 9. Interview Script

I would explain it like this:

First, I need to clarify that the problem is not asking me to maximize the total difference between `nums1[i]` and `nums2[i]`. It only asks me to maximize the number of positions where `nums1[i] > nums2[i]`.

A brute force approach would be to try all permutations of `nums1` and calculate the advantage for each one. But that would be factorial time, so it is impossible for large input sizes.

The optimized idea is greedy. I sort `nums1`, and I also sort `nums2`, but I keep each value’s original index because the answer must be returned in the original `nums2` order.

Then I always look at the smallest remaining value in `nums1`.

If this smallest `nums1` value can beat the smallest remaining `nums2` value, I use it there. This gives me a win using the cheapest possible number.

If it cannot beat the smallest remaining `nums2`, then it cannot beat any remaining `nums2` value, because all others are bigger or equal. So I sacrifice it against the largest remaining `nums2`.

I repeat this until all values are placed.

The pattern is greedy with sorting and two pointers. Sorting allows me to compare the easiest and hardest remaining values. The greedy decision is safe because I either take the cheapest win or sacrifice a value that cannot win anyway.

The time complexity is `O(n log n)` because of sorting, and the space complexity is `O(n)` for the result and sorted `nums2` pairs.

## 10. Edge Cases and Dry Run

### Edge cases

#### Case 1: All nums1 values can win

```python
nums1 = [5, 6, 7]
nums2 = [1, 2, 3]
```

Every value can be placed to win.

#### Case 2: No nums1 value can win

```python
nums1 = [1, 2, 3]
nums2 = [5, 6, 7]
```

All values are sacrifices.

#### Case 3: Equal values

```python
nums1 = [2, 2, 2]
nums2 = [2, 2, 2]
```

No wins, because the condition is strictly:

```python
nums1[i] > nums2[i]
```

Equal does not count.

#### Case 4: Duplicates in nums2

```python
nums2 = [5, 5, 5]
```

This is why we should not use a dictionary keyed only by `nums2` values.

### Dry run

Input:

```python
nums1 = [12, 24, 8, 32]
nums2 = [13, 25, 32, 11]
```

Sort `nums1`:

```python
[8, 12, 24, 32]
```

Sort `nums2` with original indices:

```python
[(11, 3), (13, 0), (25, 1), (32, 2)]
```

Start:

```python
left = 0      # nums1[left] = 8
left2 = 0     # smallest nums2 = 11
right2 = 3    # largest nums2 = 32
```

Step 1:

```python
8 > 11  # false
```

So `8` cannot beat anyone. Sacrifice it against `32`.

```python
result[2] = 8
```

Step 2:

```python
12 > 11  # true
```

Use `12` to beat `11`.

```python
result[3] = 12
```

Step 3:

```python
24 > 13  # true
```

Use `24` to beat `13`.

```python
result[0] = 24
```

Step 4:

```python
32 > 25  # true
```

Use `32` to beat `25`.

```python
result[1] = 32
```

Final result:

```python
[24, 32, 8, 12]
```

Comparisons:

```python
24 > 13  # win
32 > 25  # win
8 > 32   # lose
12 > 11  # win
```

Advantage = `3`.

## 11. Key Takeaways

* The problem asks for maximum number of wins, not maximum total difference.
* A win is only based on:

```python
nums1[i] > nums2[i]
```

* Sort `nums1` so you can use the smallest useful value.
* Sort `nums2` with original indices so you can place answers correctly.
* If smallest `nums1` can beat smallest `nums2`, take the cheap win.
* If it cannot, sacrifice it against largest `nums2`.
* Your final approach is interview-expected.
* The main pattern is:

```text
Greedy + Sorting + Two Pointers
```

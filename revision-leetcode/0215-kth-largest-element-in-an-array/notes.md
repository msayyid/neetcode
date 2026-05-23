## 215. Kth Largest Element in an Array - Revision Notes

## 1. Problem Summary

We are given an integer array `nums` and an integer `k`.

We need to return the `kth` largest element in the array.

Important detail:

```text
kth largest means sorted-order position, not kth distinct value.
```

Example:

```text
nums = [3,2,3,1,2,4,5,5,6], k = 4

Sorted descending:
[6,5,5,4,3,3,2,2,1]

4th largest = 4
```

Important constraints:

```text
1 <= k <= nums.length <= 10^5
```

Because `n` can be large, sorting works but the problem asks us to think about non-sorting approaches.

---

# 2. My Initial Understanding

You correctly understood that this problem can be solved using a heap.

Your first idea was:

```text
Use a max heap and pop k times.
```

Since Python only has a min heap by default, you converted values to negative numbers.

That was correct.

Then you improved it by using:

```text
A min heap of size k
```

This is also correct and is usually the cleaner heap solution for this problem.

---

# 3. Mistakes / Confusions I Had

## Confusion 1: Complexity of min heap approach

You were thinking:

```text
Maybe it is n + k log k?
```

But the correct time is:

```text
O(n log k)
```

Why?

Because we loop through all `n` numbers.

For each number, we may push into a heap of size at most `k + 1`.

So each heap operation costs:

```text
O(log k)
```

Since this happens for `n` numbers:

```text
O(n log k)
```

---

## Confusion 2: Why heap size k is enough

In the min heap approach, we only keep the largest `k` elements seen so far.

The smallest among those `k` largest elements is at the top of the heap.

So after processing all numbers:

```text
heap[0] = kth largest element
```

Because if something smaller than the current top appears, it will not survive inside the heap.

---

# 4. Things I Learned

## Key idea

A heap is useful when we do not need the whole sorted array.

We only need one ranked element:

```text
kth largest
```

So we can use a heap to keep only the useful part.

---

## Python heap detail

Python's `heapq` is a min heap.

So:

```python
heapq.heappop(heap)
```

always removes the smallest value.

To simulate a max heap:

```python
heap = [-n for n in nums]
```

Then the smallest negative number represents the largest original number.

Example:

```text
nums = [3, 6, 2]

negative heap values:
[-3, -6, -2]

smallest negative = -6
original value = 6
```

---

# 5. Pattern Recognition

## Main pattern

```text
Heap / Priority Queue
```

## Trigger: when should I think of heap?

Think of a heap when the problem asks for:

```text
kth largest
kth smallest
top k elements
k most frequent
smallest/largest k items
```

The clue is the word:

```text
k
```

especially when we do not need the entire array sorted.

## Why heap applies here

We do not need all numbers in sorted order.

We only need the element that would appear at a specific position if sorted.

So instead of sorting everything, we can use a heap to repeatedly extract or maintain the top `k`.

---

# 6. Approach 1 - Max Heap Using Negative Values

## Main idea

Convert all numbers into negative values so Python's min heap acts like a max heap.

Then pop from the heap `k` times.

The `kth` popped value is the kth largest number.

---

## Step-by-step algorithm

1. Create a new list where every number is negated.
2. Convert that list into a heap using `heapify`.
3. Pop from the heap `k` times.
4. The last popped negative value represents the kth largest number.
5. Return its positive version.

---

## Pseudocode

```text
create heap with all numbers negated
heapify(heap)

repeat k times:
    ans = pop from heap

return -ans
```

---

## Time complexity

```text
O(n + k log n)
```

Why?

```text
Creating negative list: O(n)
Heapify: O(n)
Each pop: O(log n)
We pop k times: O(k log n)
```

Total:

```text
O(n + k log n)
```

---

## Space complexity

```text
O(n)
```

Because we store all `n` numbers inside the heap.

---

## Why this works

The largest number becomes the smallest negative number.

So every pop gives us the next largest original number.

After popping `k` times, we get the kth largest.

---

## Limitations

This stores the entire array in the heap.

So space is:

```text
O(n)
```

Also, if `k` is small, popping from a heap of size `n` is less efficient than keeping a heap of size `k`.

---

## Interview expectation

This approach is correct and acceptable.

But it is not the cleanest heap approach.

It is a good starting heap solution.

---

# 7. Approach 2 - Min Heap of Size k

## Main idea

Keep only the largest `k` elements seen so far.

The heap is a min heap, so the smallest among those `k` largest elements stays at the top.

At the end:

```text
heap[0] = kth largest
```

---

## Step-by-step algorithm

1. Create an empty min heap.
2. Loop through every number in `nums`.
3. Push the current number into the heap.
4. If heap size becomes greater than `k`, pop the smallest value.
5. After processing all numbers, return `heap[0]`.

---

## Pseudocode

```text
heap = empty min heap

for num in nums:
    push num into heap

    if heap size > k:
        pop smallest from heap

return heap[0]
```

---

## Time complexity

```text
O(n log k)
```

Why?

We process all `n` numbers.

For each number, heap operations cost:

```text
O(log k)
```

because the heap size never grows beyond `k + 1`.

So:

```text
O(n log k)
```

---

## Space complexity

```text
O(k)
```

Because the heap only stores the largest `k` elements.

---

## Why this works

The heap keeps the best `k` candidates for largest values.

Whenever the heap grows bigger than `k`, we remove the smallest value.

That means smaller values are removed, and only the largest `k` values survive.

At the end, the heap contains the `k` largest elements.

The smallest among those `k` largest elements is the kth largest overall.

That smallest value is at:

```text
heap[0]
```

---

## Limitation

This is better than the max heap approach when `k` is small.

But if `k` is close to `n`, then:

```text
O(n log k)
```

becomes close to:

```text
O(n log n)
```

There is also a more advanced approach called Quickselect with average `O(n)`, but we are leaving that for now.

---

## Interview expectation

This is interview-expected for the heap approach.

It is cleaner than the max heap version because:

```text
Max heap version: O(n) space
Min heap size k: O(k) space
```

and usually better time when `k` is much smaller than `n`.

---

# 8. Optimized Heap Approach

The optimized heap approach is:

```text
Min heap of size k
```

Why it is better:

| Approach                |             Time |  Space | Interview status       |
| ----------------------- | ---------------: | -----: | ---------------------- |
| Max heap with negatives | `O(n + k log n)` | `O(n)` | Acceptable             |
| Min heap of size k      |     `O(n log k)` | `O(k)` | Expected heap solution |

The min heap approach is better because it avoids storing unnecessary elements.

---

# 9. Edge Cases

## Edge case 1: k = 1

```text
nums = [3,2,1,5,6,4], k = 1
```

Return the largest element.

Output:

```text
6
```

## Edge case 2: k = len(nums)

```text
nums = [3,2,1,5,6,4], k = 6
```

Return the smallest element.

Output:

```text
1
```

## Edge case 3: duplicates

```text
nums = [3,2,3,1,2,4,5,5,6], k = 4
```

Duplicates count normally.

Sorted descending:

```text
[6,5,5,4,3,3,2,2,1]
```

Output:

```text
4
```

---

# 10. Small Dry Run - Min Heap of Size k

```text
nums = [3,2,1,5,6,4], k = 2
```

We keep the largest `2` elements.

```text
Add 3 -> [3]
Add 2 -> [2,3]
Add 1 -> [1,3,2] -> size > 2, pop 1 -> [2,3]
Add 5 -> [2,3,5] -> size > 2, pop 2 -> [3,5]
Add 6 -> [3,5,6] -> size > 2, pop 3 -> [5,6]
Add 4 -> [4,6,5] -> size > 2, pop 4 -> [5,6]
```

Final heap:

```text
[5,6]
```

The largest 2 elements are:

```text
5 and 6
```

The smallest among them is:

```text
5
```

So the 2nd largest is:

```text
5
```

---

# 11. Interview Script

First, I would mention the simple sorting idea.

"I could sort the array in descending order and return the element at index `k - 1`, but that would take `O(n log n)`, and the problem asks if we can solve it without sorting."

Then explain the heap idea.

"A better approach is to use a heap. Since we only need the kth largest, we do not need the full sorted order."

For the max heap approach:

"One option is to simulate a max heap by pushing negative values into Python's min heap. Then I pop from the heap `k` times. The kth popped value is the kth largest. This takes `O(n + k log n)` time and `O(n)` space."

For the optimized min heap approach:

"The cleaner heap solution is to maintain a min heap of size `k`. I iterate through every number and push it into the heap. If the heap grows beyond size `k`, I remove the smallest element. This way, the heap always contains the largest `k` elements seen so far. At the end, the top of the heap is the smallest among the largest `k` elements, which is exactly the kth largest."

Complexity:

"This approach takes `O(n log k)` time and `O(k)` space."

---

# 12. Key Takeaways

```text
- Python heapq is a min heap.
- To simulate max heap, use negative values.
- Max heap approach: pop k times.
- Min heap size k approach: keep only the largest k elements.
- In min heap size k, heap[0] is the kth largest.
- Time for min heap size k is O(n log k), not O(n + k log k).
- This is an interview-expected heap solution.
- Quickselect is more optimal on average, but heap is easier and very acceptable.
```

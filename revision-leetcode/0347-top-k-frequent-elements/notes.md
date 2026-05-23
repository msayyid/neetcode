# 347. Top K Frequent Elements - Revision Notes

## 1. Problem Summary

We are given an array `nums` and an integer `k`.

We need to return the `k` most frequent elements.

Example:

```python
nums = [1,1,1,2,2,3]
k = 2
```

Frequencies:

```text
1 appears 3 times
2 appears 2 times
3 appears 1 time
```

So the answer is:

```python
[1, 2]
```

The answer can be returned in any order.

Key constraint:

```text
nums.length <= 10^5
```

So an `O(n log n)` solution may work practically, but the follow-up asks for better than `O(n log n)`.

---

# 2. My Initial Understanding

You first understood that the main job is to count how often each number appears.

That part was correct:

```python
freq = Counter(nums)
```

You also correctly realized that once we have frequencies, we need a way to get the largest `k` frequencies.

Your first instinct was to use a heap, which is a valid and common approach.

Then you improved it by limiting the heap size to `k`, which was also a good step.

Finally, you reached the optimized bucket sort idea, where the frequency itself becomes the index.

---

# 3. Mistakes I Made

## Mistake 1: Thinking the first heap solution was optimal

Your first heap solution puts all unique elements into the heap.

```python
heapq.heappush(heap, (-val, key))
```

This works, but the heap can contain all unique elements.

So if there are `m` unique numbers, heap operations cost:

```text
O(log m)
```

That gives:

```text
O(n + m log m)
```

Worst case:

```text
O(n log n)
```

So it does not satisfy the follow-up.

---

## Mistake 2: Trying to manually keep a list sorted

You tried this kind of idea:

```python
if res[-1][1] < val:
```

The issue is that comparing only with the last element does not keep the whole list sorted.

For example:

```text
res = [(1, 1), (2, 1), (3, 1)]
new = (4, 10)
```

The new item should go to the front, but checking only the last item is not enough.

If you scan the whole list each time to insert correctly, it becomes:

```text
O(m^2)
```

So that approach is inefficient.

---

## Mistake 3: Mixing up bucket meaning

At first, you created:

```python
count = [0] * (len(nums) + 1)
```

and tried:

```python
count[i] = freq[i]
```

That means:

```text
index = number
value = frequency
```

But for bucket sort, we need the opposite idea:

```text
index = frequency
value = list of numbers with that frequency
```

Correct idea:

```python
count = [[] for _ in range(len(nums) + 1)]
```

Then:

```python
count[val].append(key)
```

Meaning:

```text
number key appears val times
put key into bucket[val]
```

---

# 4. Things I Learned

## Key idea 1: Frequency counting is the first step

For this problem, always start with:

```python
freq = Counter(nums)
```

This gives:

```text
number -> frequency
```

Example:

```python
nums = [1,1,1,2,2,3]
```

Gives:

```text
1 -> 3
2 -> 2
3 -> 1
```

---

## Key idea 2: Heap can be used to get top k

A heap is useful when we need the largest or smallest elements.

For top `k` frequent elements, we can either:

1. Put everything into a max heap and pop `k` times.
2. Keep a min heap of size `k`.

The second one is better when `k` is small.

---

## Key idea 3: Frequency is bounded by `n`

No number can appear more than `n` times.

So if:

```text
n = len(nums)
```

then possible frequencies are:

```text
1 to n
```

This allows us to create buckets of size `n + 1`.

---

## Key idea 4: Bucket sort avoids comparison sorting

Instead of sorting by frequency, we directly place numbers into buckets.

```text
bucket[frequency] = numbers with that frequency
```

Example:

```text
bucket[1] = [3]
bucket[2] = [2]
bucket[3] = [1]
```

Then scan from the back because higher index means higher frequency.

---

# 5. Pattern Recognition

## Main pattern

```text
Bucket Sort / Frequency Bucket
```

## Trigger: how to recognize this pattern

Think about bucket sort when:

```text
You need top k based on counts/frequencies
```

and:

```text
The frequency range is bounded by n
```

In this problem:

```text
max frequency <= len(nums)
```

That is the big clue.

Because frequency cannot be larger than `n`, we can create an array of buckets where the index represents frequency.

## Why this pattern applies here

We are not sorting actual values.

We are sorting by how often values appear.

The frequency is a small bounded range:

```text
0 to n
```

So we can avoid `O(n log n)` sorting and use buckets instead.

## Similar problem types

This pattern appears in problems like:

```text
Top K Frequent Words
Sort Characters By Frequency
Group items by count
Find most common elements
Frequency-based ranking
```

---

# 6. Approaches Tried

# Approach 1: Max Heap With All Unique Elements

## Main idea

Count all frequencies, push every unique number into a max heap, then pop `k` times.

Python only has a min heap, so we use negative frequency:

```python
(-frequency, number)
```

This makes the largest frequency come out first.

## Step-by-step algorithm

1. Count frequencies using `Counter`.
2. Create an empty heap.
3. Push every `(negative frequency, number)` pair into the heap.
4. Pop from the heap `k` times.
5. Return the popped numbers.

## Pseudocode

```text
freq = Counter(nums)
heap = []

for num, count in freq:
    push (-count, num) into heap

result = []

repeat k times:
    count, num = pop heap
    add num to result

return result
```

## Time complexity

Let:

```text
n = length of nums
m = number of unique elements
```

Counting:

```text
O(n)
```

Pushing `m` items into heap:

```text
O(m log m)
```

Popping `k` items:

```text
O(k log m)
```

Total:

```text
O(n + m log m + k log m)
```

Since `k <= m`:

```text
O(n + m log m)
```

Worst case, `m = n`:

```text
O(n log n)
```

## Space complexity

```text
O(m)
```

Because we store:

```text
Counter: O(m)
Heap: O(m)
Result: O(k)
```

Overall:

```text
O(m)
```

Worst case:

```text
O(n)
```

## Why this works

The heap always gives the element with the highest frequency first because we store negative frequencies.

## Limitation

It does not satisfy the follow-up in the worst case because it can become:

```text
O(n log n)
```

## Interview expected?

This is acceptable as a first solution, but not the optimized follow-up solution.

---

# Approach 2: Min Heap of Size K

## Main idea

Instead of storing all unique elements in the heap, keep only the current top `k`.

The heap stores:

```python
(frequency, number)
```

This is a min heap.

When heap size becomes greater than `k`, remove the smallest frequency.

That way, the heap keeps only the `k` most frequent elements seen so far.

## Step-by-step algorithm

1. Count frequencies using `Counter`.
2. Create an empty min heap.
3. For each unique number:

   * Push `(frequency, number)` into heap.
   * If heap size becomes greater than `k`, pop one item.
4. At the end, the heap contains the top `k` frequent elements.
5. Return the numbers from the heap.

## Pseudocode

```text
freq = Counter(nums)
heap = []

for num, count in freq:
    push (count, num) into heap

    if heap size > k:
        pop from heap

result = []

for count, num in heap:
    add num to result

return result
```

## Time complexity

Counting:

```text
O(n)
```

Loop through `m` unique elements.

Each heap operation costs:

```text
O(log k)
```

because heap size never grows beyond `k`.

Total:

```text
O(n + m log k)
```

Worst case, if `m = n`:

```text
O(n log k)
```

If `k` is much smaller than `n`, this is much better than the first heap approach.

## Space complexity

```text
O(m + k)
```

Counter takes:

```text
O(m)
```

Heap takes:

```text
O(k)
```

Result takes:

```text
O(k)
```

Since `k <= m`, this is usually simplified to:

```text
O(m)
```

Worst case:

```text
O(n)
```

## Why this works

The heap keeps removing the least frequent element whenever we have more than `k`.

So after checking all numbers, only the `k` most frequent numbers remain.

## Limitation

If `k` is close to `n`, then:

```text
log k ≈ log n
```

So worst-case time can still be close to:

```text
O(n log n)
```

It is better than approach 1 when `k` is small, but it is not the best possible follow-up solution.

## Interview expected?

Yes, this is a strong and valid interview solution.

But for this problem’s follow-up, the bucket sort solution is more optimal.

---

# Approach 3: Bucket Sort / Frequency Buckets

## Main idea

Instead of sorting by frequency, use frequency as an index.

Create buckets where:

```text
bucket[frequency] = list of numbers with that frequency
```

Then scan from high frequency to low frequency and collect numbers until we have `k`.

## Step-by-step algorithm

1. Count frequencies using `Counter`.
2. Create `n + 1` empty buckets.
3. For each number and frequency:

   * Put the number into `bucket[frequency]`.
4. Scan buckets from the end to the start.
5. Add numbers to result.
6. Stop when result size is `k`.

## Pseudocode

```text
freq = Counter(nums)
bucket = array of empty lists with size n + 1

for num, count in freq:
    bucket[count].append(num)

result = []

for i from n down to 1:
    for num in bucket[i]:
        result.append(num)

        if len(result) == k:
            return result
```

## Time complexity

Counting frequencies:

```text
O(n)
```

Building buckets:

```text
O(m)
```

Scanning buckets:

```text
O(n)
```

Total:

```text
O(n)
```

This satisfies the follow-up.

## Space complexity

Counter:

```text
O(m)
```

Buckets:

```text
O(n)
```

Result:

```text
O(k)
```

Overall:

```text
O(n)
```

## Why this works

Frequency is bounded by `n`.

So instead of sorting frequencies, we directly place each number into the bucket matching its frequency.

The highest frequencies are at the highest indexes.

Scanning from the end gives the most frequent elements first.

## Limitation

Uses extra `O(n)` bucket space.

But that is acceptable for this problem.

## Interview expected?

Yes. This is the optimized expected solution for the follow-up.

---

# 7. Optimized Approach

The optimized approach is:

```text
Bucket Sort / Frequency Bucket
```

It is better than heap because it avoids `log` operations.

Heap solutions need comparisons:

```text
O(log m) or O(log k)
```

Bucket sort avoids comparison-based sorting by using frequency as an index.

The key reason it works:

```text
Maximum frequency is at most n
```

So we can create:

```python
count = [[] for _ in range(len(nums) + 1)]
```

Then:

```python
count[val].append(key)
```

Meaning:

```text
put number key into the bucket for frequency val
```

Then scan from the end.

Final optimized complexity:

```text
Time: O(n)
Space: O(n)
```

---

# 8. Final Code

You asked for notes and included the final code already, so no need to rewrite the full code again.

Your final bucket solution is correct and interview-expected.

Cleaner detail: using `len(result) == k` is better than using a separate counter.

You already did that in the final version:

```python
if len(result) == k:
    return result
```

Good.

---

# 9. Interview Script

## Brute force / first heap explanation

“I would first count the frequency of each number using a hashmap. Then I can push all unique numbers into a max heap based on frequency. Since Python has a min heap, I store negative frequencies. After that, I pop from the heap `k` times to get the `k` most frequent elements.”

“The time complexity is `O(n + m log m)`, where `m` is the number of unique elements. In the worst case, this becomes `O(n log n)`, so it works but does not satisfy the follow-up.”

---

## Improved heap explanation

“To improve the heap approach, I can keep a min heap of size `k`. I push each `(frequency, number)` pair into the heap. If the heap size becomes bigger than `k`, I remove the smallest frequency. At the end, the heap contains only the top `k` frequent elements.”

“This improves the heap part to `O(m log k)` because the heap size is only `k`. The total time is `O(n + m log k)`. This is good when `k` is small, but if `k` is close to `n`, it can still be close to `O(n log n)`.”

---

## Optimized bucket sort explanation

“The optimized solution uses bucket sort. After counting frequencies, I know that no number can appear more than `n` times. So I create `n + 1` buckets, where the index represents frequency.”

“For example, if number `5` appears `3` times, I put `5` into `bucket[3]`. After placing all numbers into buckets, I scan the buckets from the end to the beginning, because higher index means higher frequency. I collect numbers until I have `k` elements.”

“This gives `O(n)` time because we count once, build buckets once, and scan the buckets once. The space complexity is `O(n)`.”

---

# 10. Edge Cases and Dry Run

## Edge cases

### Case 1: Only one element

```python
nums = [1]
k = 1
```

Answer:

```python
[1]
```

---

### Case 2: All elements same

```python
nums = [5,5,5,5]
k = 1
```

Frequency:

```text
5 -> 4
```

Answer:

```python
[5]
```

---

### Case 3: All elements unique

```python
nums = [1,2,3]
k = 2
```

Every frequency is `1`.

Any valid `2` elements can be returned, depending on problem guarantee/order.

---

### Case 4: Multiple numbers have different frequencies

```python
nums = [1,1,1,2,2,3]
k = 2
```

Frequencies:

```text
1 -> 3
2 -> 2
3 -> 1
```

Buckets:

```text
bucket[1] = [3]
bucket[2] = [2]
bucket[3] = [1]
```

Scan from back:

```text
bucket[3] -> take 1
bucket[2] -> take 2
```

Result:

```python
[1, 2]
```

---

# 11. Key Takeaways

## Main things to remember

1. Start with frequency counting:

```python
freq = Counter(nums)
```

2. Max heap with all elements is correct but can be:

```text
O(n log n)
```

3. Min heap of size `k` improves it to:

```text
O(n + m log k)
```

4. Bucket sort is the optimized follow-up solution:

```text
O(n)
```

5. Bucket sort works because:

```text
frequency is bounded by n
```

6. The important mental switch is:

```text
Do not store frequency by number.
Store numbers by frequency.
```

Meaning:

```text
bucket[frequency] = list of numbers
```

## Final pattern trigger

When the problem asks for:

```text
top k frequent elements
```

and frequency cannot exceed `n`, think:

```text
Can I use frequency as an index?
```

That is the clue for bucket sort.

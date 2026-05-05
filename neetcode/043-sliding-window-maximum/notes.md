# Sliding Window Maximum - Revision Notes

## 1. Problem Summary

You are given:

```python
nums = [1, 2, 1, 0, 4, 2, 6]
k = 3
```

You need to look at every window of size `k` and return the maximum value from each window.

Example:

```text
[1, 2, 1] -> 2
[2, 1, 0] -> 2
[1, 0, 4] -> 4
[0, 4, 2] -> 4
[4, 2, 6] -> 6
```

Output:

```python
[2, 2, 4, 4, 6]
```

### Key idea

Instead of recalculating the maximum for every window, we can keep track of useful maximum candidates using a monotonic deque.

### Important constraints

```text
1 <= nums.length <= 100,000
1 <= k <= nums.length
```

Because `n` can be up to `100,000`, an `O(n * k)` solution can be too slow.

---

# 2. My Initial Understanding

Your first solution used a normal sliding window with `left` and `right`.

For every window, you calculated:

```python
max(nums[left:right + 1])
```

You correctly understood:

```text
The while loop runs for each window.
There are about n windows in the worst case.
Finding max inside each window takes k time.
So total time is O(n * k).
```

You also noticed that slicing creates extra memory.

Then you improved it by manually scanning the window instead of slicing.

That version had the same time complexity but better auxiliary space.

---

# 3. Mistakes I Made

## Mistake 1: Thinking slicing version has only O(1) extra space

Your first version:

```python
max(nums[left:right + 1])
```

creates a new temporary list of size `k`.

So auxiliary space is:

```text
O(k)
```

It is not `O(1)`.

---

## Mistake 2: Confusion about `deque.pop()`

You were unsure whether:

```python
q.pop()
```

removes from the front or back.

Correction:

```python
q.pop()       # removes from the back/right
q.popleft()   # removes from the front/left
```

For this problem:

```python
q.pop()
```

removes smaller useless candidates from the back.

```python
q.popleft()
```

removes expired candidates from the front.

---

## Mistake 3: Thinking the deque stores only the max element

The deque does not store only one max.

It stores indices of possible maximum values.

Better wording:

```text
The deque stores indices of useful maximum candidates.
The values are kept in decreasing order.
The front of the deque is always the current maximum.
```

Example:

```text
nums = [5, 3, 2]
deque values = [5, 3, 2]
```

`5` is the current max, but `3` and `2` are kept because they may become max after `5` leaves.

---

## Mistake 4: Confusion about the main idea

The main idea is not just “use deque”.

The real idea is:

```text
If a newer value is bigger than an older value, the older value becomes useless.
```

Example:

```text
1, 2
```

Once `2` appears, `1` can never be the maximum in any future window containing both `1` and `2`.

So we remove `1`.

---

# 4. Things I Learned

## Deque operations

Python `deque` supports efficient operations on both ends:

```python
q.append(x)      # add to back, O(1)
q.pop()          # remove from back, O(1)
q.appendleft(x)  # add to front, O(1)
q.popleft()      # remove from front, O(1)
```

A beginner-friendly mental model:

```text
A deque is like a structure designed for fast adding/removing from both ends.
It feels similar to a linked list at the ends because it does not shift elements like a normal list.
```

But Python’s deque is not exactly a linked list. Internally, it uses blocks.

---

## Why normal list is not good for front removal

With a normal Python list:

```python
arr.pop(0)
```

is `O(n)` because all elements need to shift left.

With deque:

```python
q.popleft()
```

is `O(1)`.

---

## Why store indices instead of values?

We store indices because we need to know whether an element is outside the current window.

Example:

```text
nums = [5, 3, 2, 1]
k = 3
```

First window:

```text
[5, 3, 2]
```

Max is `5`.

Next window:

```text
[3, 2, 1]
```

Now `5` is outside the window.

If we only stored value `5`, we would not know whether it is still inside.
By storing index `0`, we can check whether it is expired.

---

## Why the deque is decreasing

The deque keeps values in decreasing order.

Example:

```text
deque values = [5, 4, 1]
```

This means the maximum is always at the front:

```python
nums[q[0]]
```

So getting the current max becomes `O(1)`.

---

# 5. Pattern Recognition

## Main pattern

```text
Sliding Window + Monotonic Deque
```

## Trigger: how to recognize this pattern

Think of monotonic deque when the problem says:

```text
Find maximum/minimum in every sliding window/subarray of fixed size k.
```

Important clues:

```text
1. There is a fixed-size window.
2. The window moves one step at a time.
3. You need max or min repeatedly.
4. Brute force recalculates max/min and becomes O(n * k).
5. You need to reuse information from previous windows.
```

## Why this pattern applies here

Each window overlaps heavily with the previous one.

Example:

```text
[1, 2, 1]
   [2, 1, 0]
```

Most elements are reused. Only one old element leaves and one new element enters.

So instead of scanning the whole window again, we maintain a deque of useful candidates.

## Similar problem types

This pattern appears in problems like:

```text
Maximum in every subarray of size k
Minimum in every subarray of size k
Shortest subarray with constraints
Sliding window with max/min tracking
Problems requiring “current best value” while a window moves
```

---

# 6. Approaches Tried

## Approach 1: Brute Force with Slicing

### Main idea

For every window, slice the array and use `max()`.

### Step-by-step algorithm

```text
1. Set left = 0 and right = k - 1.
2. While right is inside the array:
   - Take nums[left:right + 1].
   - Find max of that slice.
   - Append it to result.
   - Move left and right by 1.
3. Return result.
```

### Pseudocode

```text
result = []

left = 0
right = k - 1

while right < len(nums):
    window = nums[left : right + 1]
    result.append(max(window))
    left += 1
    right += 1

return result
```

### Time complexity

There are `n - k + 1` windows.

Each `max()` scans `k` elements.

```text
O(n * k)
```

### Space complexity

The slice creates a temporary list of size `k`.

```text
Auxiliary space: O(k)
Including result: O(n)
```

### Why it works

It directly checks every window and finds the maximum.

### Limitation

It is too slow for large input.

Also, slicing creates extra memory.

### Interview expectation

This is a valid starting/brute force approach, but not interview-expected for a Hard problem.

---

## Approach 2: Brute Force without Slicing

### Main idea

Instead of slicing, manually scan from `left` to `right`.

This avoids creating a temporary list.

### Step-by-step algorithm

```text
1. Set left = 0 and right = k - 1.
2. While right is inside the array:
   - Set max_element = nums[left].
   - Loop from left to right.
   - Update max_element.
   - Append max_element to result.
   - Move left and right by 1.
3. Return result.
```

### Pseudocode

```text
result = []

left = 0
right = k - 1

while right < len(nums):
    max_element = nums[left]

    for i from left to right:
        max_element = max(max_element, nums[i])

    result.append(max_element)

    left += 1
    right += 1

return result
```

### Time complexity

Still scans `k` elements for every window.

```text
O(n * k)
```

### Space complexity

No slicing, only one variable.

```text
Auxiliary space: O(1)
Including result: O(n)
```

### Why it works

It checks every window and manually calculates the maximum.

### Limitation

Still too slow because it recalculates the max from scratch for every window.

### Interview expectation

Better brute force than slicing in terms of memory, but still not optimal.

---

## Approach 3: Optimized Monotonic Deque

### Main idea

Use a deque to store indices of possible maximum values.

The deque keeps values in decreasing order.

That means:

```text
nums[q[0]] is always the maximum of the current window.
```

### Step-by-step algorithm

```text
1. Create an empty result list.
2. Create an empty deque q.
3. Use right to scan through nums.
4. For every nums[right]:
   - Remove indices from the back while their values are smaller than nums[right].
   - Append right to the deque.
   - Remove the front index if it is outside the current window.
   - If the window is valid, append nums[q[0]] to result.
   - Move the window forward.
5. Return result.
```

### Pseudocode

```text
result = []
q = empty deque

left = 0
right = 0

while right < len(nums):

    while q is not empty and nums[q.back] < nums[right]:
        q.pop_back()

    q.push_back(right)

    if q.front < left:
        q.pop_front()

    if right + 1 >= k:
        result.append(nums[q.front])
        left += 1

    right += 1

return result
```

### Time complexity

```text
O(n)
```

Why?

Each index is:

```text
added once
removed at most once
```

Even though there is a `while` loop, total pops across the whole algorithm are at most `n`.

### Space complexity

The deque can store at most `k` useful indices for the current window.

```text
Auxiliary space: O(k)
Including result: O(n)
```

### Why it works

The deque removes useless values.

If the current value is bigger than previous values, those previous smaller values can never be maximum again while the current value is in the window.

So we remove them.

The deque also removes expired values from the front when they leave the window.

### Limitation

The logic is harder to understand than brute force.

### Interview expectation

This is the interview-expected optimal solution.

---

# 7. Optimized Approach Explanation

Your final optimized solution uses:

```text
Sliding Window + Monotonic Deque
```

The deque stores indices, not values.

Why indices?

```text
Because we need to know whether an element is outside the current window.
```

The deque is monotonic decreasing by value.

Example:

```text
deque values = [6, 4, 2]
```

This means the maximum is always at the front.

When a new number enters, we remove smaller values from the back.

Example:

```text
Current deque values: [5, 3, 2]
New value: 4
```

`2` is smaller than `4`, so remove it.

`3` is smaller than `4`, so remove it.

`5` is bigger than `4`, so keep it.

New deque values:

```text
[5, 4]
```

This is why the max is always easy to get.

```python
nums[q[0]]
```

---

# 8. Final Code

You asked for notes, but since you shared your final cleaned code, here is the cleaner final version with required import:

```python
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()  # stores indices of possible maximum values

        left = right = 0

        while right < len(nums):
            # Remove smaller values from the back.
            # They are useless because nums[right] is bigger and newer.
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # Add current index as a possible maximum candidate.
            q.append(right)

            # Remove front index if it is outside the current window.
            if left > q[0]:
                q.popleft()

            # Once the window size reaches k, record the maximum.
            if right + 1 >= k:
                result.append(nums[q[0]])
                left += 1

            right += 1

        return result
```

Your code is correct and interview-expected.

One small cleaner alternative is this condition:

```python
if q[0] < left:
    q.popleft()
```

It means the same thing as:

```python
if left > q[0]:
    q.popleft()
```

But many people find `q[0] < left` easier to read as:

```text
if the index is before the left boundary, remove it
```

---

# 9. Interview Script

## Brute force explanation

“I first thought about checking every window independently. Since each window has size `k`, I can scan the window and find the maximum. There are `n - k + 1` windows, and each scan takes `O(k)`, so the total time is `O(n * k)`. This works, but it is too slow when `n` is large.”

## Improved brute force without slicing

“To reduce memory usage, instead of slicing the window, I can manually loop from `left` to `right` and track the maximum. This keeps auxiliary space at `O(1)`, but the time complexity is still `O(n * k)` because I still scan each window fully.”

## Optimized explanation

“The optimized approach uses a monotonic deque. The deque stores indices of elements, and the values of those indices are kept in decreasing order. This means the front of the deque always gives the maximum of the current window.”

“When a new value enters the window, I remove smaller values from the back of the deque because they can never become maximum while this newer and larger value is still in the window. Then I add the current index.”

“I also check whether the index at the front is outside the current window. If it is, I remove it. Once the window size reaches `k`, I append `nums[q[0]]` to the result because that is the current maximum.”

“Each index is added once and removed at most once, so the time complexity is `O(n)`. The deque stores at most `k` indices, so auxiliary space is `O(k)`.”

---

# 10. Edge Cases and Dry Run

## Important edge cases

### Case 1: `k = 1`

Every window has one element.

```python
nums = [4, 2, 7]
k = 1
```

Output:

```python
[4, 2, 7]
```

Each element is its own maximum.

---

### Case 2: `k = len(nums)`

Only one window exists.

```python
nums = [1, 3, 2]
k = 3
```

Output:

```python
[3]
```

---

### Case 3: Decreasing array

```python
nums = [5, 4, 3, 2, 1]
k = 3
```

Deque keeps multiple values because each older larger value may remain the max until it leaves.

Output:

```python
[5, 4, 3]
```

---

### Case 4: Increasing array

```python
nums = [1, 2, 3, 4, 5]
k = 3
```

Each new value removes all smaller previous values.

Output:

```python
[3, 4, 5]
```

---

### Case 5: Duplicate values

```python
nums = [2, 2, 2]
k = 2
```

Output:

```python
[2, 2]
```

Your code uses:

```python
nums[q[-1]] < nums[right]
```

not:

```python
nums[q[-1]] <= nums[right]
```

So equal values are kept. This is fine and correct.

---

## Dry run

```python
nums = [1, 2, 1, 0, 4]
k = 3
```

### Start

```text
result = []
q = []
left = 0
right = 0
```

### right = 0, value = 1

Add index `0`.

```text
q indices = [0]
q values = [1]
```

No full window yet.

---

### right = 1, value = 2

`2` is bigger than `1`, so remove index `0`.

Add index `1`.

```text
q indices = [1]
q values = [2]
```

No full window yet.

---

### right = 2, value = 1

`1` is smaller than `2`, so keep both.

```text
q indices = [1, 2]
q values = [2, 1]
```

Now window is valid:

```text
[1, 2, 1]
```

Max is:

```text
nums[q[0]] = nums[1] = 2
```

Result:

```text
[2]
```

Move `left` to `1`.

---

### right = 3, value = 0

`0` is smaller than `1`, so keep it.

```text
q indices = [1, 2, 3]
q values = [2, 1, 0]
```

Window:

```text
[2, 1, 0]
```

Max:

```text
2
```

Result:

```text
[2, 2]
```

Move `left` to `2`.

---

### right = 4, value = 4

`4` is bigger than `0`, remove `0`.

`4` is bigger than `1`, remove `1`.

`4` is bigger than `2`, remove `2`.

Add index `4`.

```text
q indices = [4]
q values = [4]
```

Window:

```text
[1, 0, 4]
```

Max:

```text
4
```

Result:

```text
[2, 2, 4]
```

Final output for this shortened example:

```python
[2, 2, 4]
```

---

# 11. Key Takeaways

```text
1. Brute force scans every window, so it is O(n * k).
2. Slicing version also uses O(k) temporary space.
3. Manual brute force avoids slicing, so auxiliary space becomes O(1), but time is still O(n * k).
4. Optimized solution uses a monotonic deque.
5. The deque stores indices, not values.
6. The deque values are kept in decreasing order.
7. The front of the deque is always the current maximum.
8. Remove smaller values from the back because they are no longer useful.
9. Remove expired values from the front because they left the window.
10. Final optimized time is O(n), auxiliary space is O(k).
```

The most important sentence to remember:

```text
A monotonic deque keeps only useful maximum candidates in decreasing order, so the front always gives the maximum of the current sliding window.
```

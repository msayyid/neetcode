# LeetCode 1004: Max Consecutive Ones III - Revision Notes

## 1. Problem Summary

We are given a binary array `nums` containing only `0`s and `1`s.

We can flip at most `k` zeros into ones.

We need to return the maximum length of consecutive `1`s possible after doing those flips.

### Simple meaning

Find the longest subarray where the number of `0`s is at most `k`.

Because if a subarray has at most `k` zeros, we can flip all those zeros into ones.

### Key idea

Instead of actually flipping zeros, we just count how many zeros are inside the current window.

If the window has more than `k` zeros, it becomes invalid, so we move the left pointer until the window is valid again.

### Important constraints

```text
1 <= nums.length <= 10^5
nums[i] is either 0 or 1
0 <= k <= nums.length
```

Because `n` can be up to `100,000`, an `O(n^2)` solution is too slow.

We need an `O(n)` solution.

---

# 2. My Initial Understanding

Your first idea was close to sliding window.

You were thinking:

```text
Count consecutive 1s.
Use k replacements when seeing 0s.
When replacements are used up, move left.
Track max length.
```

This is the right direction because the problem is about a changing window.

You understood correctly that:

* We need to track a continuous subarray.
* We can allow up to `k` zeros inside that subarray.
* We should move `left` when the window becomes invalid.
* This should be a sliding window problem.

Where you got confused:

* You tried to separately process runs of `1`s and runs of `0`s.
* You used `can_replace`, which made the logic harder to manage.
* You were shrinking based on the current `nums[right]`, instead of shrinking based on the real condition: `zeros > k`.

---

# 3. Mistakes I Made

## Mistake 1: Splitting the logic into separate while loops

Your first version had logic like:

```python
while nums[right] == 1:
    ...
```

and then another loop for zeros.

The issue is that a valid window can contain mixed values:

```text
1 0 1 1 0 1
```

So treating ones and zeros as separate phases makes the code complicated.

The cleaner idea is:

```text
For every right pointer:
    Add nums[right] into the window
    If window is invalid, shrink from left
    Update answer
```

---

## Mistake 2: Risk of index error

This part was dangerous:

```python
while nums[right] == 1:
```

because `right` could become equal to `len(nums)`, and then `nums[right]` would crash.

Whenever using `nums[right]`, we must make sure:

```python
right < len(nums)
```

---

## Mistake 3: Shrinking based on `nums[right]`

You had logic like:

```python
if left < right and can_replace < k and nums[right] == 0:
```

The problem is that shrinking should not depend only on `nums[right]`.

The correct reason to shrink is:

```text
The window has more than k zeros.
```

So the real condition is:

```python
while zeros > k:
```

This is the most important correction.

---

## Mistake 4: Worrying that nested while means `O(n^2)`

You were unsure whether this part makes the solution quadratic:

```python
while zeros > k:
    ...
    left += 1
```

It does not.

Even though there is a `while` inside a `for` loop, the `left` pointer only moves forward.

Across the whole algorithm:

```text
right moves at most n times
left moves at most n times
```

So total time is:

```text
O(n + n) = O(n)
```

---

# 4. Things I Learned

## Key concept

This problem can be rephrased as:

```text
Find the longest subarray with at most k zeros.
```

That makes the solution much easier.

---

## Valid window condition

A window is valid when:

```text
zeros <= k
```

A window is invalid when:

```text
zeros > k
```

So the algorithm is:

```text
Expand right.
Count zeros.
If zeros > k, move left until valid.
Update max length.
```

---

## Why we count zeros instead of flipping

We do not need to actually change the array.

If a window has `k` or fewer zeros, then those zeros can be flipped.

So counting zeros is enough.

---

## Important formula

Current window length:

```python
right - left + 1
```

This works because both `left` and `right` are inclusive pointers.

---

# 5. Pattern Recognition

## Main pattern

Sliding Window.

## Trigger: how to recognize it

Think of sliding window when the problem asks for:

```text
maximum/minimum length of a contiguous subarray
```

and there is a condition like:

```text
at most k bad elements
at most k changes
at most k distinct values
sum less than or equal to target
```

Here, the clue is:

```text
maximum number of consecutive 1s
```

That means we care about a contiguous subarray.

Another clue is:

```text
flip at most k zeros
```

That means the window is allowed to contain at most `k` bad elements.

The "bad elements" are zeros.

So the problem becomes:

```text
Longest window with at most k zeros.
```

That is a classic sliding window trigger.

---

## Why sliding window applies here

When we move `right`, the window grows.

If the window has too many zeros, we move `left` until the window becomes valid again.

This works because moving `left` forward can only remove elements from the current window. It helps reduce the number of zeros.

---

## Similar problem types

This same pattern appears in problems like:

* Longest substring with at most `k` distinct characters
* Longest substring after replacing at most `k` characters
* Longest subarray with at most `k` bad elements
* Maximum consecutive answers after changing at most `k`
* Longest subarray with sum less than or equal to target, when numbers are non-negative

---

# 6. Approaches Tried

## Approach 1: Manual counting with `can_replace`

### Main idea

Your first approach tried to:

* Count consecutive ones.
* Use `can_replace` when seeing zeros.
* Move `left` when flips were used up.
* Track current length manually.

### Step-by-step idea

```text
Start left and right at 0.
Move right while seeing 1s.
When seeing 0s, use available replacements.
Track length.
If replacements run out, move left.
Update max length.
```

### Pseudocode

```text
left = 0
right = 0
can_replace = k
length = 0

while right < n:
    consume all 1s
    consume 0s while can_replace > 0
    update max_length

    if need to shrink:
        move left
        update can_replace and length
```

### Time complexity

In theory, this could be made `O(n)`.

### Space complexity

```text
O(1)
```

### Why this approach is incomplete

The idea is close, but the implementation becomes messy because the window can contain mixed zeros and ones.

You were managing too many states:

```text
left
right
length
can_replace
max_length
```

Also, shrinking was based on special cases instead of the simple invalid-window rule.

### Interview expected?

Not in this form.

The idea is sliding window, but the code is not clean enough for interviews.

---

## Approach 2: Standard sliding window with zero count

### Main idea

Maintain a window where the number of zeros is at most `k`.

If the window has more than `k` zeros, move `left` until it becomes valid again.

### Step-by-step algorithm

```text
1. Set left = 0.
2. Set zeros = 0.
3. Set max_length = 0.
4. Loop right from 0 to n - 1.
5. If nums[right] is 0, increase zeros.
6. While zeros > k:
       If nums[left] is 0, decrease zeros.
       Move left forward.
7. Now the window is valid.
8. Update max_length using right - left + 1.
9. Return max_length.
```

### Pseudocode

```text
left = 0
zeros = 0
max_length = 0

for right in range(n):
    if nums[right] == 0:
        zeros += 1

    while zeros > k:
        if nums[left] == 0:
            zeros -= 1
        left += 1

    max_length = max(max_length, right - left + 1)

return max_length
```

### Time complexity

```text
O(n)
```

`right` moves through the array once.

`left` also moves through the array once.

So total work is linear.

### Space complexity

```text
O(1)
```

Only a few variables are used.

### Why this approach works

The window always represents a possible subarray.

If the window has at most `k` zeros, we can flip those zeros and make the whole window ones.

If the window has more than `k` zeros, it is invalid, so we shrink it from the left.

Every time the window is valid, we check its length.

### Limitations

No real limitation for this problem. This is the optimal approach.

### Interview expected?

Yes.

This is the standard interview-expected solution.

---

# 7. Optimized Approach

The optimized approach is the standard sliding window solution.

The key idea is:

```text
Longest subarray with at most k zeros.
```

We use two pointers:

```text
left
right
```

`right` expands the window.

`left` shrinks the window only when there are too many zeros.

The window is valid when:

```text
zeros <= k
```

The window is invalid when:

```text
zeros > k
```

Why it is better than the earlier approach:

* No need for `length` variable.
* No need for `can_replace`.
* No need to separately handle runs of ones and zeros.
* The condition is simple and clear.
* Easier to explain in interviews.

---

# 8. Final Code

You asked for notes, and we already discussed the code, so no need to repeat the full final code here.

Your final version is correct and clean.

Cleaner standard structure:

```text
for right in range(len(nums)):
    add nums[right]
    while window invalid:
        remove nums[left]
        left += 1
    update answer
```

---

# 9. Interview Script

Here is how you can explain it in an interview:

```text
The brute force idea would be to check every possible subarray and count how many zeros it contains. If the number of zeros is less than or equal to k, then that subarray can be converted into all ones. We would keep the maximum length. But this would take O(n^2), which is too slow because nums can have up to 10^5 elements.

The optimized idea is to use a sliding window. The important observation is that we are looking for the longest contiguous subarray that contains at most k zeros. Those zeros are the ones we would flip.

I keep two pointers, left and right, and a variable zeros to count how many zeros are inside the current window. As I move right, I add nums[right] into the window. If nums[right] is zero, I increment zeros.

If zeros becomes greater than k, the window is invalid, so I move left forward until zeros is at most k again. When moving left, if nums[left] was zero, I decrease the zero count.

After the window is valid, I update the answer with right - left + 1.

This works because the window always contains at most k zeros when I update the answer, meaning all zeros in that window can be flipped to ones.

The time complexity is O(n), because right moves forward once and left also moves forward at most once. The space complexity is O(1).
```

---

# 10. Edge Cases and Dry Run

## Edge cases

### Case 1: All ones

```text
nums = [1,1,1,1], k = 2
```

Answer:

```text
4
```

No zeros need to be flipped.

---

### Case 2: All zeros

```text
nums = [0,0,0,0], k = 2
```

Answer:

```text
2
```

We can flip at most two zeros.

---

### Case 3: k = 0

```text
nums = [1,1,0,1,1,1], k = 0
```

Answer:

```text
3
```

We cannot flip any zero, so we just need the longest existing streak of ones.

---

### Case 4: k is large enough

```text
nums = [0,1,0,1], k = 2
```

Answer:

```text
4
```

We can flip both zeros.

---

## Small dry run

```text
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```

We expand the window:

```text
[1,1,1,0,0]
```

Zeros = 2, valid.

Length = 5.

Then we include another zero:

```text
[1,1,1,0,0,0]
```

Zeros = 3, invalid.

Now we move `left` until one zero is removed from the window.

Eventually the window becomes valid again with at most 2 zeros.

Later, the best valid window becomes:

```text
[0,0,1,1,1,1]
```

Length = 6.

Answer:

```text
6
```

---

# 11. Key Takeaways

* This problem is not really about flipping manually.
* It is about finding the longest subarray with at most `k` zeros.
* The trigger for sliding window is:

```text
maximum consecutive / longest contiguous subarray + at most k changes
```

* Use `zeros` to track how many bad elements are inside the window.
* Shrink only when:

```python
zeros > k
```

* Current window length is:

```python
right - left + 1
```

* Nested `while` does not mean `O(n^2)` here because both pointers only move forward.
* Final complexity:

```text
Time: O(n)
Space: O(1)
```

* Your final solution is interview-expected.

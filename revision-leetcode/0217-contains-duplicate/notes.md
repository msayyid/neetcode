# LeetCode 217 - Contains Duplicate Notes

## 1. Problem Summary

We are given an integer array `nums`.

We need to return:

```text
True  -> if any number appears at least twice
False -> if every number is unique
```

Example:

```text
nums = [1, 2, 3, 1]
```

`1` appears twice, so the answer is `True`.

Key idea:

We need to detect whether we have seen the same number before.

Important constraints:

```text
1 <= nums.length <= 100000
-10^9 <= nums[i] <= 10^9
```

Because `nums.length` can be up to `100000`, an `O(n^2)` brute force solution is too slow. We need an `O(n)` or `O(n log n)` approach.

---

# 2. My Initial Understanding

You understood the main idea correctly:

* Duplicates mean some value appears more than once.
* A dictionary or set can be used to remember values.
* If we see a value again, we can return `True`.
* If we finish checking everything, return `False`.

You tried several approaches:

1. Count all frequencies using a dictionary.
2. Use a dictionary and return early.
3. Use a set and return early.
4. Use `len(set(nums)) != len(nums)`.

Your understanding improved from “count every number” to “we only need to know if we have seen this number before.”

That is the important optimization.

---

# 3. Mistakes I Made

## Mistake 1: Counting everything before checking for duplicates

Your first solution:

```python
counter = dict()

for n in nums:
    counter[n] = counter.get(n, 0) + 1

for val in counter.values():
    if val > 1:
        return True
```

This works, but it does extra work.

Why?

If the duplicate appears early, for example:

```text
nums = [1, 1, 2, 3, 4, 5]
```

You do not need to count the whole array. As soon as you see the second `1`, you can return `True`.

So this solution is correct, but not the cleanest.

---

## Mistake 2: Using a dictionary when a set is enough

In your second solution, you used a dictionary:

```python
counter = dict()
```

But you were not really using the count.

You only needed to check:

```python
if n in counter:
```

That means the value itself matters, not the number of times it appears.

A `set` is better because it is designed for membership checking.

Better:

```python
seen = set()
```

---

## Mistake 3: Leaving debug prints in the final solution

Your first solution had:

```python
print(counter)
```

This is fine while debugging, but should be removed before submitting.

In interviews and LeetCode submissions, debug prints can make the solution look unfinished.

---

# 4. Things I Learned

## 1. HashSet is the natural tool for duplicate detection

When a problem asks:

```text
Have I seen this value before?
```

Think of a set.

A set allows fast membership checking:

```python
if n in seen:
```

Average time: `O(1)`.

---

## 2. Dictionary is useful when we need counts

Use a dictionary when the problem asks for frequency, for example:

```text
How many times does each number appear?
Which number appears most often?
Does every number appear exactly k times?
```

But this problem only asks whether a duplicate exists.

So a set is enough.

---

## 3. Early return improves practical performance

Instead of checking the whole array, we can return immediately when a duplicate is found.

Example:

```text
nums = [5, 5, 1, 2, 3, 4]
```

The answer is known after checking the second element.

This does not change worst-case Big O, but it makes the solution cleaner and often faster.

---

## 4. `set(nums)` removes duplicates

Example:

```python
nums = [1, 2, 3, 1]
set(nums) = {1, 2, 3}
```

So if:

```python
len(set(nums)) != len(nums)
```

then some duplicate must have been removed.

---

# 5. Pattern Recognition

## Main Pattern: HashSet / HashMap

The main pattern is:

```text
HashSet for seen values
```

## Trigger: What clue tells me to use this pattern?

The problem asks:

```text
Does any value appear at least twice?
```

This means we need to check whether a value has appeared before.

That is the main clue.

Whenever you see phrases like:

```text
duplicate
appears twice
seen before
unique values
contains repeated value
```

you should think about using a set or hashmap.

## Why this pattern applies here

We scan the array once.

For each number:

* If it is already in the set, we found a duplicate.
* If it is not in the set, we add it.

This gives fast checking because set membership is average `O(1)`.

## Similar problem types

This pattern appears in problems like:

* Contains Duplicate II
* Valid Anagram
* Two Sum
* First Unique Character
* Intersection of Two Arrays
* Longest Consecutive Sequence
* Find Duplicate Number, although that one can have extra constraints

---

# 6. Approaches Tried

## Approach 1: Frequency Dictionary

### Main idea

Count how many times each number appears, then check if any count is greater than `1`.

### Step-by-step algorithm

1. Create an empty dictionary called `counter`.
2. Loop through every number in `nums`.
3. Increase the count of that number.
4. After counting everything, loop through the dictionary values.
5. If any value is greater than `1`, return `True`.
6. Otherwise, return `False`.

### Pseudocode

```text
counter = empty dictionary

for num in nums:
    counter[num] += 1

for count in counter values:
    if count > 1:
        return True

return False
```

### Time complexity

```text
O(n)
```

We loop through the array once and then through the dictionary values.

`O(n) + O(n) = O(n)`.

### Space complexity

```text
O(n)
```

In the worst case, all numbers are unique, so the dictionary stores all `n` numbers.

### Why this works

If a number appears more than once, its count will become greater than `1`.

### Limitations

It does unnecessary work because it counts every number before checking for duplicates.

### Interview expected?

It is correct, but not the best interview answer. It is more of a starting approach.

---

## Approach 2: Dictionary with Early Return

### Main idea

Use a dictionary to remember numbers we have already seen. Return `True` immediately when we see a repeated number.

### Step-by-step algorithm

1. Create an empty dictionary.
2. Loop through every number.
3. If the number is already in the dictionary, return `True`.
4. Otherwise, add it to the dictionary.
5. If the loop finishes, return `False`.

### Pseudocode

```text
seen = empty dictionary

for num in nums:
    if num in seen:
        return True

    seen[num] = 1

return False
```

### Time complexity

```text
O(n)
```

Each lookup and insert is average `O(1)`.

### Space complexity

```text
O(n)
```

In the worst case, all numbers are unique.

### Why this works

A duplicate means we are seeing a number that was already stored before.

### Limitations

A dictionary works, but it is slightly unnecessary because we do not need counts or key-value pairs.

### Interview expected?

Good, but a set is cleaner.

---

## Approach 3: Set with Early Return

### Main idea

Use a set to store numbers we have seen. If we see the same number again, return `True`.

### Step-by-step algorithm

1. Create an empty set called `seen`.
2. Loop through each number in `nums`.
3. If the number is already in `seen`, return `True`.
4. Otherwise, add the number to `seen`.
5. If the loop finishes, return `False`.

### Pseudocode

```text
seen = empty set

for num in nums:
    if num in seen:
        return True

    add num to seen

return False
```

### Time complexity

```text
O(n)
```

Set lookup and insertion are average `O(1)`.

### Space complexity

```text
O(n)
```

In the worst case, the set stores all numbers.

### Why this works

The set keeps track of every number we have already visited.

If a number is already in the set, that means it appeared before.

### Limitations

Uses extra memory.

### Interview expected?

Yes. This is the best standard interview solution.

---

## Approach 4: Compare Length of List and Set

### Main idea

Convert the list into a set. Since a set removes duplicates, compare the length of the set with the length of the original list.

### Step-by-step algorithm

1. Convert `nums` into a set.
2. Compare the length of the set with the length of `nums`.
3. If the lengths are different, return `True`.
4. Otherwise, return `False`.

### Pseudocode

```text
if length of set(nums) != length of nums:
    return True
else:
    return False
```

Or simply:

```text
return length of set(nums) != length of nums
```

### Time complexity

```text
O(n)
```

Building the set takes `O(n)` average time.

### Space complexity

```text
O(n)
```

The set may store all numbers.

### Why this works

If there are duplicates, the set will remove them.

Example:

```text
nums = [1, 2, 3, 1]
set(nums) = {1, 2, 3}
```

Original length is `4`, set length is `3`, so a duplicate exists.

### Limitations

It does not return early. It always builds the full set.

It is very Pythonic, but it does not show the algorithmic thinking as clearly as the loop-based set approach.

### Interview expected?

Acceptable in Python, but for interviews, explain the set early-return version.

---

# 7. Optimized Approach

## Final optimized solution: HashSet with Early Return

The best solution is:

```text
Use a set to remember seen numbers.
Return True as soon as a repeated number appears.
```

Why it is better:

* Cleaner than using a dictionary.
* Does not count unnecessary frequencies.
* Can stop early.
* Easy to explain in an interview.

Pattern used:

```text
HashSet / Seen Set
```

Why this pattern applies:

The problem is asking whether a value has appeared before. A set is perfect for fast membership checks.

Time complexity:

```text
O(n)
```

Space complexity:

```text
O(n)
```

---

# 8. Final Code

You did ask for notes, so no full final code is needed here.

But the cleaner standard version is the set early-return approach.

---

# 9. Interview Script

Here is a natural way to explain it:

```text
First, I could solve this by comparing every pair of numbers and checking if any two are equal. But that would take O(n^2), which is too slow because the array can have up to 100,000 elements.

A better approach is to use a set. I will scan through the array once and keep track of the numbers I have already seen.

For each number, I check if it is already in the set. If it is, then I have found a duplicate, so I return True immediately.

If it is not in the set, I add it and continue.

If I finish the loop without finding any repeated number, then all elements are distinct, so I return False.

This works because a duplicate means the same value appears again later in the array, and the set lets me check whether I have seen a value before in O(1) average time.

The time complexity is O(n), because we visit each number once. The space complexity is O(n), because in the worst case all numbers are unique and stored in the set.
```

For the one-line Python version:

```text
Another Pythonic way is to compare len(nums) with len(set(nums)). Since a set removes duplicates, if the lengths are different, then duplicates existed. This is also O(n) time and O(n) space, but in an interview I would explain the explicit set approach because it shows the logic more clearly.
```

---

# 10. Edge Cases and Dry Run

## Edge cases

### 1. Only one element

```text
nums = [1]
```

There cannot be a duplicate.

Answer:

```text
False
```

---

### 2. Duplicate at the beginning

```text
nums = [1, 1, 2, 3]
```

Return `True` quickly after seeing the second `1`.

---

### 3. Duplicate at the end

```text
nums = [1, 2, 3, 4, 1]
```

We scan almost the whole array before finding the duplicate.

---

### 4. All elements unique

```text
nums = [1, 2, 3, 4]
```

Return `False`.

---

### 5. Negative numbers

```text
nums = [-1, -2, -3, -1]
```

Still works because sets can store negative integers too.

---

## Dry run

Input:

```text
nums = [1, 2, 3, 1]
```

Start:

```text
seen = {}
```

Step 1:

```text
n = 1
1 not in seen
add 1

seen = {1}
```

Step 2:

```text
n = 2
2 not in seen
add 2

seen = {1, 2}
```

Step 3:

```text
n = 3
3 not in seen
add 3

seen = {1, 2, 3}
```

Step 4:

```text
n = 1
1 is already in seen
return True
```

Final answer:

```text
True
```

---

# 11. Key Takeaways

* When the problem asks about duplicates, think about a set.
* Use a dictionary when you need counts.
* Use a set when you only need to know whether something has appeared before.
* Early return is better than counting everything first.
* `len(set(nums)) != len(nums)` is a clean Python shortcut.
* The best interview explanation is the set early-return approach.
* Time complexity: `O(n)`
* Space complexity: `O(n)`

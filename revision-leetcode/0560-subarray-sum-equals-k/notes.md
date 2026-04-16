# Subarray Sum Equals K

## Problem

Given an integer array `nums` (can include negative numbers) and an integer `k`:

👉 Return the number of **continuous subarrays** whose sum equals `k`.

---

# Key Observations

* Elements can be **negative** → sliding window does **NOT** work
* We need to count **ALL subarrays**, including overlapping ones
* Multiple subarrays can end at the same index

---

# Approach 1: Brute Force

## Idea

* Try **every possible subarray**
* Use two loops:

  * `i` → start
  * `j` → end
* Accumulate sum dynamically

---

## Algorithm

```text
for each i:
    total = 0
    for each j from i → end:
        total += nums[j]
        if total == k:
            count += 1
```

---

## Why it works

* It checks **all possible (i, j)** pairs
* So it finds:

  * overlapping subarrays
  * all valid sums

---

## Complexity

* Time: `O(n²)`
* Space: `O(1)`

---

## Key Understanding

👉 `total` is reused to avoid recomputing sums

---

## Limitation

* Too slow for large inputs
* Repeats a lot of work

---

# Approach 2: Prefix Sum + HashMap (Optimal)

## Core Idea

Instead of fixing start:

👉 Fix the **end index** and find how many valid starts exist

---

## Prefix Sum Definition

```text
prefix[i] = sum of nums[0 → i]
```

---

## Key Formula

```text
subarray_sum = prefix[i] - prefix[j]
```

We want:

```text
prefix[i] - prefix[j] = k
```

Rearrange:

```text
prefix[j] = prefix[i] - k
```

---

## Intuition

At each index:

👉 “Have I seen a prefix sum equal to `current_sum - k` before?”

If yes:

→ each occurrence = 1 valid subarray

---

## Data Structure

```text
map = { prefix_sum : frequency }
```

---

## Algorithm

```text
initialize map = {0: 1}
total = 0
count = 0

for each num:
    total += num

    complement = total - k

    if complement exists:
        count += frequency of complement

    store/update total in map
```

---

## Why `{0:1}`?

👉 Handles subarrays starting at index 0

Example:

```text
nums = [3], k = 3
```

* total = 3
* total - k = 0 → found → valid subarray

---

## Why frequency (not just existence)?

Because:

👉 same prefix sum can appear multiple times

Each occurrence = different valid subarray

---

## Why order matters?

Correct:

```text
check first → then update map
```

Wrong order leads to:

* counting current prefix as previous
* invalid / duplicate subarrays

---

## Complexity

* Time: `O(n)`
* Space: `O(n)`

---

# Why Sliding Window Fails

Sliding window requires:

* expand → sum increases
* shrink → sum decreases

❌ Not true with negative numbers

Example:

```text
nums = [2, -1, 2]
```

* expanding can decrease sum
* shrinking can increase sum

👉 window becomes unpredictable

---

# Mental Model (Important)

At every index:

👉 “How many previous prefix sums can pair with me to form k?”

---

# Comparison

| Approach       | Time  | Space | Works with negatives |
| -------------- | ----- | ----- | -------------------- |
| Brute Force    | O(n²) | O(1)  | Yes                  |
| Prefix + Map   | O(n)  | O(n)  | Yes                  |
| Sliding Window | O(n)  | O(1)  | ❌ No                 |

---

# Key Takeaways

* This is a **prefix sum + hashmap pattern**
* Very similar to:

  * Two Sum (but on prefix sums)
* Core trick:

```text
current_sum - k
```

NOT:

```text
k - current_sum
```

---

# Interview Tips

If asked:

👉 Start with brute force
👉 Explain why sliding window fails
👉 Derive prefix sum formula
👉 Then present hashmap solution

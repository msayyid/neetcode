# Pivot Index - Notes (ChatGPT)

## Problem

Find index `i` such that:

* sum of elements before `i` == sum of elements after `i`

---

# Approach 1 - Brute Force (O(n^2))

## Idea

For every index:

* calculate left sum using a loop
* calculate right sum using another loop
* compare them

## Logic

For each `i`:

* left = sum(nums[0 → i-1])
* right = sum(nums[i+1 → end])
* if left == right → return `i`

## Complexity

* Time: O(n^2)
* Space: O(1)

## Why it works

* Directly computes what problem asks
* No tricks, just brute checking

## Downsides

* Recomputes sums again and again
* Too slow for large inputs → TLE

---

# Mistakes I Made

* Initially forgot to reset `left` and `right`
* Used `return -1` inside loop → exited too early
* Didn’t realize nested loops = O(n^2)
* Didn’t think about reusing previous computations

---

# Approach 2 - Optimized (Prefix Sum Idea) (O(n))

## Key Insight

Instead of recalculating right sum every time:

* Use total sum
* Derive right sum using math

---

## Core Formula

```
total = left + current + right
→ right = total - left - current
```

So condition becomes:

```
left_sum == total_sum - left_sum - nums[i]
```

---

## Idea

* Compute total sum once
* Keep a running `left_sum`
* At each index:

  * compute right using formula
  * compare
  * update left_sum

---

## Logic Flow

For each `i`:

1. Check:

   * left_sum == total_sum - left_sum - nums[i]
2. If yes → return `i`
3. Update:

   * left_sum += nums[i]

---

## Complexity

* Time: O(n)
* Space: O(1)

---

## Why this is better

* No nested loops
* No repeated work
* Uses math instead of recomputation

---

# Key Insight (Important)

We are NOT storing right sum.

We are **calculating it instantly** using:

```
right = total - left - current
```

---

# Mental Model

```
[ left ] [ i ] [ right ]
```

We know:

```
total = left + i + right
```

So:

```
right = total - left - i
```

Then:

```
if left == right → pivot
```

---

# Common Pitfalls

* Updating `left_sum` before checking → wrong
* Skipping index 0 → incorrect (it can be pivot)
* Forgetting that `nums[i]` should NOT be included in left or right
* Overthinking formula instead of deriving from total

---

# Final Takeaway

* Brute force → understand problem
* Optimized → avoid recomputation
* Pattern → **running sum + total sum**
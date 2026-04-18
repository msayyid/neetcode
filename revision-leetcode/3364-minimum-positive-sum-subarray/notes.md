# Minimum Positive Sum Subarray - Brute Force Notes

## Goal

Find a subarray such that:

* length is between `l` and `r` (inclusive)
* sum **> 0**
* among all valid ones → return **minimum sum**

If none → return `-1`

---

## Core idea (brute force)

Try **every possible subarray** and check if it satisfies conditions.

Use:

* `i` → start index
* `j` → end index

Build subarrays from `i → j`

---

## Key optimization (important)

Instead of recomputing sum every time:

❌ Bad:

```python
sum(nums[i:j+1])   # O(n) each time → O(n³)
```

✅ Good:

* maintain running sum
* expand window by adding next element

---

## Pattern

For each `i`:

* reset `total = 0`
* expand `j` from `i → n-1`
* keep adding to `total`

---

## Window properties

### Length

```id="len_rule"
window_length = j - i + 1
```

Must satisfy:

```id="len_check"
l ≤ window_length ≤ r
```

---

### Sum condition

```id="sum_rule"
total > 0
```

Only consider **strictly positive**

---

## Update answer

If both conditions pass:

```id="update_rule"
res = min(res, total)
```

---

## Edge case

If no valid subarray found:

```id="edge_case"
return -1
```

---

## Time complexity

* Outer loop: `n`
* Inner loop: `n`

```id="complexity"
O(n²)
```

Acceptable because:

```id="constraint"
n ≤ 100
```

---

## What you did well

* Used incremental sum → avoids O(n³)
* Correct length calculation
* Correct filtering (`> 0`)
* Proper min tracking
* Handled no-answer case

---

## Common mistakes (you already hit one)

### 1. Wrong element added

```id="mistake1"
total += nums[i]   ❌
```

Should follow **expanding pointer (`j`)**

---

### 2. Mixing pointers with constraints

* `l`, `r` = rules
* `i`, `j` = movement

Never mix them

---

### 3. Thinking sliding window works here

* negatives exist → breaks monotonic behavior
* brute force is safer baseline

---

## Small mental improvement (optional)

Once:

```id="break_rule"
window_length > r
```

You can **stop inner loop early** for that `i`
(because length will only increase)

---

## One-line memory

> Fix start `i`, expand `j`, build sum, check length and positivity, keep minimum.

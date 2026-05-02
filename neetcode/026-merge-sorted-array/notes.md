**Problem:** Merge two sorted arrays into `nums1` in-place, given `m` valid elements in `nums1` and `n` elements in `nums2`.

---

**Approach 1 (naive):**
Replace the placeholder zeros in `nums1` with values from `nums2`, then sort.

```python
for i in range(m, m + n):
    nums1[i] = nums2[i - m]
nums1.sort()
```

- Zeros start at index `m`, so `range(m, m+n)` targets them directly
- `nums2[i - m]` avoids a redundant `j` pointer — `i - m` measures how far past `m` we are
- Time: O((n+m) log(n+m)), Space: O(1)

---

**Approach 2 (optimal):**
Merge from the back, exploiting the fact that both arrays are already sorted.

```python
last = m + n - 1
m, n = m - 1, n - 1
while n >= 0:
    if m >= 0 and nums1[m] > nums2[n]:
        nums1[last] = nums1[m]
        m -= 1
    else:
        nums1[last] = nums2[n]
        n -= 1
    last -= 1
```

- Start `last` at end of `nums1`, `m-1` and `n-1` as last valid indices of each array
- Compare from the back, placing the larger element at `last` and decrementing accordingly
- Loop only on `n >= 0` — if `m` runs out, `nums1` elements are already in place, but `nums2` leftovers still need placing
- Guard the `if` with `m >= 0` so when `m` is exhausted it falls to `else` and keeps placing `nums2` elements
- `last -= 1` is common to both branches so it lives outside the `if/else`
- Time: O(n+m), Space: O(1)

---

**Mistakes I had:**
- First naive attempt only replaced at `i == m-1` instead of the full range `range(m, m+n)`
- Used `m > 0 and n > 0` instead of `>= 0` in the while condition, missing the element at index 0

**New things learnt:**
- Merging from the back avoids overwriting valid elements in `nums1`
- When both arrays are already sorted, you can avoid sorting entirely and get O(n+m)
- Common logic inside both `if/else` branches can be pulled out to avoid repetition
- Two while loops can sometimes be merged into one by rethinking the loop condition and adding a guard inside

**Contains Nearby Duplicate**

**Problem:** Given an array `nums` and integer `k`, return `True` if there are two indices `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

---

**Approach (Sliding Window Set):**
The idea is to maintain a window (set) of at most `k` elements. At any point, if the current element already exists in the window, it means we saw it within the last `k` indices — so we return `True`.

---

**Why a set?**
Sets are hash-based, so checking membership (`in`) and removing elements are both **O(1)** average case. There are no indices in a set — only values (hashes).

---

**The sliding window logic:**
- We add `nums[i]` to the window every iteration
- Once `i >= k`, the window would grow beyond `k` elements, so we remove the element that is now too far away
- That element is `nums[i - k]` — the value we added exactly `k` steps ago
- **Important:** we are removing by **value** from the set, not by index. `nums[i-k]` gives us the value that needs to leave
- This is different from popping — we're saying "remove this specific value" not "remove from position"
- The window slides forward with `i`, so the element that becomes too far changes every step — `nums[i-k]` always points to exactly the right one

---

**Key insight — the window size enforces the distance constraint implicitly:**
This was a confusing point at first. You don't need to explicitly check `abs(i - j) <= k`. The window holding at most `k` elements does this for you automatically.

Example: `nums = [1,2,3,1], k = 3`
- At `i=3`, window is `{1, 2, 3}` — these came from indices `0, 1, 2`
- We find `nums[3] = 1` already in the window
- The furthest back it could have been added is index `3 - 3 = 0`
- Distance = `abs(3 - 0) = 3` which is `<= k` ✓
- The window size guarantees this is always true — anything further than `k` steps ago has already been evicted

Initial confusion was thinking it only works for cases like `[1,2,1,3]` — but the window handles `[1,2,3,1]` too because `3-0=3` is still within `k`.

---

**Step by step each iteration:**
```
1. Check if nums[i] already in window → return True
2. Add nums[i] to window
3. If i >= k → remove nums[i - k] from window (it's now too far)
```

---

**Pseudocode:**
```
window = empty set

for i in range(len(nums)):
    if nums[i] in window:
        return True
    
    add nums[i] to window
    
    if i >= k:
        remove nums[i - k] from window

return False
```

---

**Complexities:**
- Time: O(n) — single pass through the array
- Space: O(k) — window holds at most `k` elements at any time

---

**Things to remember:**
- Sets have no indices, only hashes — removal is by value not position
- `nums[i - k]` is the value we added `k` steps ago — it's now outside the valid range so we evict it
- The window slides forward, so what's "too far" changes every step — it's not always `nums[0]`
- The window size itself enforces `abs(i-j) <= k` — you never need to check distances explicitly
- Check membership **before** adding to the window, otherwise you'd always find the element you just added
**Subarray Sum Equals K**
**Difficulty:** Medium
**Time:** O(n) | **Space:** O(n)

---

**What I tried first:**
Brute force with two loops — `i` as the start, `j` extending the subarray, accumulating a running sum from `i` to `j` and checking if it equals `k`. That works but is O(n²).

**Mistakes I made in brute force:**
- Used `k` for two different things (loop variable and target)
- `j` wasn't starting relative to `i`
- Had a `break` which stopped counting further valid subarrays from the same start
- Forgot to always add `nums[i]` to total regardless of whether it equals `k`

**Optimal approach — Prefix Sums + Hashmap:**

A prefix sum at index `j` is the running total from index 0 to j. The sum of any subarray from `i` to `j` is `prefix[j] - prefix[i]`. So instead of checking every pair, at each index we ask: *"how many previous positions can start a subarray that ends here and sums to k?"* The map answers that instantly.

**Why `{0:1}` to start:**
0 represents curSum before the loop starts, so we don't miss subarrays starting from index 0.

**Key rules:**
- Always check the map BEFORE updating it — map must only contain past sums
- Add `map[diff]` not `+1` — the value tells you how many valid starts exist

**Final clean solution:**
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_map = {0: 1}  # 0:1 represents curSum before loop starts, so we don't miss subarrays starting from index 0
        cur_sum = 0  # keeps record of prefixes
        res = 0  # actual count
        for num in nums:
            cur_sum += num
            diff = cur_sum - k  # look up if we have seen this before
            res += my_map.get(diff, 0)  # how many valid starts exist for this ending
            my_map[cur_sum] = my_map.get(cur_sum, 0) + 1  # update map after checking
        return res
```
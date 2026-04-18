from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = float("inf")
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                window_length = j - i + 1
                if window_length > r:
                    break
                total += nums[j]
                if window_length >= l and window_length <= r and total > 0:
                    res = min(res, total)
        if res == float("inf"): return -1
        return res

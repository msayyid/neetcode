from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total >= target:
                    min_length = min(min_length, j - i + 1)
                    break
        return 0 if min_length == float("inf") else min_length


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        min_length = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_length = min(min_length, r - l + 1)
                total -= nums[l]
                l += 1
        
        return 0 if min_length == float("inf") else min_length
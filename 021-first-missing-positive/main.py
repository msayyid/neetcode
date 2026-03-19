from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 1
        for i in range(len(nums)):
            if count not in nums_set:
                return count
            count += 1
        return count
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
            elif nums[i] - nums[i-1] == 0:
                continue
            elif nums[i] - nums[i-1] > 1:
                longest = max(longest, count)
                count = 1
        
        return max(longest, count)
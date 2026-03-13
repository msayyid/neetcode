from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest, count = 0, 1
        for i in range(1, len(nums)):
            comparison = nums[i] - nums[i-1]
            if comparison == 1:
                count += 1
            elif comparison > 1:
                longest = max(longest, count)
                count = 1
        return max(longest, count)
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        count = 0
        for n in nums:
            if n-1 not in numSet:
                count = 0
                while n+count in numSet:
                    count += 1
                longest = max(longest, count)
        return longest
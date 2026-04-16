from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1
        return count
    

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        count = 0
        my_map = {0:1}
        for i in range(len(nums)):
            total += nums[i]
            complement = total - k
            if complement in my_map:
                count += my_map[complement]
            my_map[total] = my_map.get(total, 0) + 1
        return count
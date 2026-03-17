from typing import List

# brute frorce On^2 time
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        for i in range(len(nums)):
            total = 0
            if nums[i] == k:
                    count += 1
            total += nums[i]
            for j in range(i+1, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1
        return count
    


# On time On space
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_map = dict()
        my_map[0] = 1
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            if prefix - k in my_map:
                count += my_map[prefix-k]
            my_map[prefix] = my_map.get(prefix, 0) + 1
        return count
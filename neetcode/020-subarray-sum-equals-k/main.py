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
        my_map = {0: 1}  # 0:1 represents curSum before loop starts, so we don't miss subarrays starting from index 0
        cur_sum = 0  # keeps record of prefixes
        res = 0  # actual count
        for num in nums:
            cur_sum += num
            diff = cur_sum - k  # look up if we have seen this before
            res += my_map.get(diff, 0)  # how many valid starts exist for this ending
            my_map[cur_sum] = my_map.get(cur_sum, 0) + 1  # update map after checking
        return res
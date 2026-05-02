from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * len(nums)
        # build the prfix
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]

        # map to store how many times each prefix sum has appeared
        # {prefix_sum : frequency}
        # start with {0:1} to handle subarrays starting from index 0
        my_map = {0:1}
        count = 0 # total number of subarrays with sum = k

        # go through each prefix sum
        for i in range(len(nums)):
            # we want: prefix[i] - prevous_prefix = k
            # so: previous_prefix = prefix[i] - k
            complement = prefix[i] - k
            
            # if this complement was seen before,
            # it means we found subarrays endint at i with sum = k
            if complement in my_map:
                # add how many times this compliment appeared
                count += my_map[complement] 

            # now add current prefix to the map
            # so it can be used for future elements  
            my_map[prefix[i]] = my_map.get(prefix[i], 0) + 1
        return count



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        my_map = {0:1}
        count = 0
        for i in range(len(nums)):
            prefix += nums[i]
            # complement = prefix - k
            if prefix - k in my_map:
                count += my_map[prefix - k]

            my_map[prefix] = my_map.get(prefix, 0) + 1

        return count
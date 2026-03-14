from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_map = dict()
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1

        res = []
        for k, v in my_map.items():
            if v > len(nums)//3:
                res.append(k)
        return res

# this one works, with linear time and linear space complexities
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    temp = []
                    if i != j and i != k and j != k:
                        if nums[i] + nums[k] + nums[j] == 0:
                            temp.append(nums[i])
                            temp.append(nums[j])
                            temp.append(nums[k])
                            temp = sorted(temp)
                            if temp not in res:
                                res.append(temp)
        return res

# brute force the above one, On^3 time and O1 space or On space n being the number of triplets


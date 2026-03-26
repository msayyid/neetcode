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



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break
            l, r = i + 1, n - 1

            while l < r:
                cur_sum = nums[l] + nums[r] + nums[i]

                if cur_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1

                elif cur_sum > 0:
                    r -= 1
                else:
                    l += 1
        return res
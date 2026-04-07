from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums
        

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        index = len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[index] = nums[l] * nums[l]
                l += 1
            else:
                res[index] = nums[r] * nums[r]
                r -= 1
            index -= 1
        return res


from typing import List

# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         # left = 0
#         # right = 0
#         for i in range(len(nums)):
#             left = 0
#             right = 0
#             # if i != 0:
#             for l in range(0, i):
#                 left += nums[l]
#             for r in range(i + 1, len(nums)):
#                 right += nums[r]

#             if left == right:
#                 return i
#         else:
#             return -1

                
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            if left_sum == right_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]       
        return -1





s = Solution()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
print(s.pivotIndex([2,1,-1]))
# print(s.pivotIndex([1, 7, 3, 6, 5, 6]))

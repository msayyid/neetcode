from typing import List


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         output = []
#         product = 1
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if j != i:
#                     product *= nums[j]
#             output.append(product)
#             product = 1
#         return output
    

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            prefix_mult[i] = product
            product *= nums[i]

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix_mult[i] *= product
            product *= nums[i]

        return prefix_mult

        



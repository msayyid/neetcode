from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

            
        for i in range(insert_pos, len(nums)):
            nums[i] = 0



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != insert_pos:
                    nums[insert_pos] = nums[i]
                insert_pos += 1

        for i in range(insert_pos, len(nums)):
            nums[i] = 0
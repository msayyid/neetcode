import random
from typing import List

class Solution:
    def sortArray(self, nums):
        self.quicksort(nums, low=0, high=len(nums)-1)
        return nums
    
    def quicksort(self, nums, low, high):
        # sort the elements in the array

        if high <= low: return # base case

        pivot = self.partition(nums, low, high)
        self.quicksort(nums, low, pivot-1)
        self.quicksort(nums, pivot+1, high)

    def partition(self, nums, low, high):
        pivot_idx = random.randint(low, high)
        nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]

        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1 # change to the pivot
        nums[i], nums[high] = nums[high], nums[i]
        return i



sol = Solution()

# Basic
print(sol.sortArray([5, 10, 2, 1, 3]))        # [1,2,3,5,10]

# Already sorted
print(sol.sortArray([1, 2, 3, 4, 5]))          # [1,2,3,4,5]

# Reverse sorted
print(sol.sortArray([5, 4, 3, 2, 1]))          # [1,2,3,4,5]

# Duplicates
print(sol.sortArray([10,9,1,1,1,2,3,1]))       # [1,1,1,1,2,3,9,10]

# Single element
print(sol.sortArray([1]))                       # [1]

# Negatives
print(sol.sortArray([-5, 3, -1, 0, -3]))       # [-5,-3,-1,0,3]

# All same
print(sol.sortArray([2, 2, 2, 2]))             # [2,2,2,2]


# merge sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            # this function splits the array into halves
            # until nothing size is 1
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2

            sorted_left = merge_sort(nums[:mid])
            sorted_right = merge_sort(nums[mid:])

            return merge(sorted_left, sorted_right)

        def merge(A, B):
            result = []
            i = 0
            j = 0
            while i < len(A) and j < len(B):
                if A[i] <= B[j]:
                    result.append(A[i])
                    i += 1
                else:
                    result.append(B[j])
                    j += 1

            while i < len(A):
                result.append(A[i])
                i += 1

            while j < len(B):
                result.append(B[j])
                j += 1

            return result

        return merge_sort(nums)
    

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        sorted_left = self.merge_sort(nums[:mid])
        sorted_right = self.merge_sort(nums[mid:])

        return self.merge(sorted_left, sorted_right)

    def merge(self, A, B):
        result = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
        
        while i < len(A):
            result.append(A[i])
            i += 1

        while j < len(B):
            result.append(B[j])
            j += 1
        
        return result
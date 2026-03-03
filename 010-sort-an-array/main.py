import random

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
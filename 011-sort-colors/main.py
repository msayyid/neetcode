# class Solution:
#     def sortColors(self, nums) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         my_map = dict()
#         for i in range(len(nums)):
#             my_map[nums[i]] = my_map.get(nums[i], 0) + 1
        
#         counter = 0
#         for i in range(3):
#             if i in my_map:

#                 for j in range(my_map[i]):
#                     nums[counter] = i
#                     counter += 1


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 1:
                mid += 1
            elif nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


# Sort Colors — Updated Notes

# Dutch National Flag Algorithm
# A one-pass algorithm that sorts an array of three distinct values in-place using three pointers: 
# low (left boundary for 0s), mid (current scanner), high (right boundary for 2s). Everything unexamined stays between mid and high.

# Solution 1: Two-Pass HashMap
# Count occurrences into a map, then overwrite nums color by color using a counter.
# Mistakes I made:

# wrote [v]*k instead of [k]*v — confused color and count
# tried to return instead of modifying nums in-place
# used my_map[nums[i]] in the second loop instead of my_map[i]
# used j as index into nums but it reset each outer loop — needed counter outside the loop
# said "swapping" but this is overwriting, not swapping

# Time: O(n) — O(n) to build map + O(n) to refill nums
# Space: O(1) — max 3 keys, 3 values, plus counter

# Solution 2: Dutch National Flag (one-pass)
# Three cases: if 1 → mid += 1. If 0 → swap with low, both low and mid move. 
# If 2 → swap with high, only high -= 1, mid stays because the swapped-in element is unknown.
# Loop condition is mid <= high not mid < high because when they meet there's still one unexamined element.

# Time: O(n) — mid only moves forward, each element visited at most once
# Space: O(1) — three pointers only
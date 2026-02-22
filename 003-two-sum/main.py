# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             print(i)
#             for j in range(i+1, len(nums)):
#                 print("i am j", j)
#                 if nums[i] + nums[j] == target:
#                     # asn = [i, j]
#                     return [i, j]



class Solution:
    def twoSum(self, nums, target):
        my_map = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_map:
                return [my_map[complement], i]
            else:
                my_map[nums[i]] = i



sol = Solution()

nums = [3,4,5,6]
target = 7
result = sol.twoSum(nums, target)
print("one",result)
nums = [4,5,6]
target = 10
result = sol.twoSum(nums, target)
print("two",result)

nums = [5,5] 
target = 10
result = sol.twoSum(nums, target)
print("three",result)


# Problem: given an array of numbers and a target, return the indices of the two numbers that add up to the target.

# Approach 1 (brute force): loop through every element, and for each element loop through the rest of the array to 
# find a pair that adds up to target. Time is O(n²) because for every element we're looping through the array again. 
# Space is O(1) since we're not creating anything extra. Also since j always starts at i+1, i is always smaller, 
# so you can just return [i, j] directly without checking order.

# Approach 2 (hashmap — optimal): the key insight is: for every number I'm looking at, I already know what number 
# I need — it's target - nums[i], the complement. So instead of searching the whole array for it, 
# I use a map to remember what I've already seen and check in O(1).

# Here's how it works step by step:

# Create an empty map that stores number → index
# For each element, calculate the complement: target - nums[i]
# Check if that complement is already in the map — if yes, we found our pair, return [my_map[complement], i]
# If no, add the current number and its index to the map and keep going

# Why [my_map[complement], i] is always in the right order: we only add things to the map after checking, 
# so if we find the complement in the map it was added in an earlier iteration — meaning its index 
# is always smaller than i. No need to check order.

# A mistake I made: I was using nums.index(complement) to get the index instead of my_map[complement]. 
# That was costing an extra O(n) lookup for each iteration, making it O(n²) again — defeating the 
# whole point of the map. The map already stores the index, use it!

# Time: O(n) — one loop, and all lookups inside are O(1).
# Space: O(n) — the map can grow up to the size of the input in the worst case, 
# unlike the anagram problem where it was capped at 26 letters.
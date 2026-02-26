def removeElement(nums, val) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [1,1,2,3,4]
val = 1
print(removeElement(nums, val))

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))


nums = [1, 2]
val = 3
print(removeElement(nums, val))


# Problem: Remove Element (In-Place)
# What the question actually wants:
# Modify the original array directly (no new array) so that all valid elements (not equal to val) are at the front. 
# Return only the count k of those elements. The grader uses k to check the first k positions of your array itself.

# Key pattern to remember:
# Whenever you see "in-place" + "return k", it means: silently do the work on the array, return just the count.
# My first mistake:
# I tried to pop and append while iterating — this causes index out of range because the list shrinks while the 
# loop range stays fixed. Never modify a list's size while iterating over it by index.
# My second attempt:
# I tried two pointers from both ends (p1 from left, p2 from right), swapping val elements with valid ones. This got complicated — 
# I was undercounting because when both pointers pointed to valid elements, moving them inward silently skipped elements on the right without counting them.

# What finally worked — single pointer approach:

# k starts at 0, acting as a placement pointer
# Loop through every element with i
# If nums[i] != val, write it to nums[k] and increment k
# At the end, k is both the count and the boundary

# New things learnt:

# "In-place" means edit the original array, not create a new one
# You can overwrite the array on itself using a slow pointer k and fast pointer i
# The slow pointer's final value IS your answer — no need to search or slice

# Time complexity: O(n) — single pass through the array
# Space complexity: O(1) — no extra space, editing in-place
def majorityElement(nums):
    # i could create a map and store teh values as keys and their appearnce as values
    # and return whichever element appears more than n/2 times in the array
    count = 1
    majority_num = nums[0]
    nums=[1,2,3,2,2,2,5,4,2]
    for i in range(1, len(nums)):
        if majority_num == nums[i]:
            count += 1
        else: count -= 1
        
        if count == 0:
            print(f"maj num before swap {majority_num} after swap - {nums[i]}")
            majority_num = nums[i]
            count = 1

    print(majority_num)
    return majority_num

nums=[1,2,3,2,2,2,5,4,2]
majorityElement(nums)

# Majority Element — Notes
# My approach: HashMap counting. Store each number as a key and its frequency as the value. 
# Loop through the map and return the key whose value exceeds n/2.

# Complexity (HashMap approach):

# Time: O(n) — one pass to build the map, one pass to scan it
# Space: O(n) — we store each unique element in the map, and there can be at most n unique elements

# Optimised approach — Boyer-Moore Voting Algorithm:
# Walk through the array once with a candidate and a count. If you see the same element as your candidate, 
# increment count. If different, decrement. If count hits 0, swap candidate to the current element 
# and reset count to 1 (because you've now seen the new candidate exactly once). 
# The majority element always outvotes the rest, so it survives at the end.

# Complexity (Boyer-Moore):

# Time: O(n) — one pass
# Space: O(1) — no extra data structures

# Bug I had: When swapping the candidate after count hit 0, I wasn't resetting count to 1. 
# I was leaving it at 0, which meant the new candidate started with an inaccurate count — as if 
# I hadn't seen it yet, when I clearly had just seen it once.


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_map = {}
        for num in nums:
            my_map[num] = my_map.get(num, 0) + 1
        
        for key, val in my_map.items():
            # integer division to avoid float comparison
            # grater than n // 2
            if val > (len(nums) // 2):
                return key
            

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else: 
                count -= 1
            if count == 0: 
                # previous candidate got fully cancelled by other elements
                # so we pick a new candidate at current position
                candidate = nums[i]
                # start with 1 because current element is the first vote
                count = 1

        return candidate
    

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                # reset candidate when no votes remain
                # DO NOT increment in here (handled below)
                candidate = num
            if candidate == num:
                # same element => +1 vote
                count += 1
            else:
                # different element => -1 vote
                count -= 1
            

        return candidate
    
# count represents net votes; majority element (> n/2) can never be fully cancelled
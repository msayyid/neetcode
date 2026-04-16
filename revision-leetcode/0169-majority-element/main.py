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
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_map = dict()
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1

        res = []
        for k, v in my_map.items():
            if v > len(nums)//3:
                res.append(k)
        return res

# this one works, with linear time and linear space complexities


class Solution:
    # solution with hashmap (boyer-moore voting algorithm) On, O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            # we are now incrementing the val of key(count[n]) by one, 
            # by deafult they are 0 thanks to defaultdict(int)
            # basically we are just populating our count
            count[n] += 1

            # now this means, do nothing (just go and keep iterating without
            # continuing) if the length is 2 or less
            if len(count) <= 2:
                continue
            
            # if the len(count) > 2:
            new_count = defaultdict(int) # this one is needed to store
            # the keys and values, where values after decrementing are still 
            # greater than 0, otherwise we would have to pop our map, 
            # which could break the loop (which is in following lines)

            for n, c in count.items():
                if c > 1: # this here is from the drawing explanation
                          # popping the map if count is zero
                          # meaning if c is bigger than 1, if we decrement
                          # we still have something (1), therefore 
                          # add new values to the new_count if only the 
                          # decremented values are > 0
                    new_count[n] = c - 1 # here we know that c - 1 is gonna 
                                         # be greater than 0 due to 
                                         # checks above
            # now after we have added the two most frequent elements 
            # to the new_count, we assign it to our own count
            count = new_count

            # this for loop does not guarantee the majority elements greater
            # than n//3, but it does guarantee the most frequent 2 elements

        # now we just verify if the values in our count are actually
        # valid > n//3
        res = []
        for n in count: # this is not a On, this is O(2), as we have at most 2 elements
            if nums.count(n) > len(nums) // 3: # in here i didn't understand the nums.count(n), are we checking how many times n appears direactly in the original array? i think it is just better to check if v > n//3 ? (i mean it does still work tho, because count in arrays is On operation, which won't affect our final time complexity)
                # we cannot use v from count.items, because it does not contain the real count of the keys
                res.append(n)
        return res
            


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # at most 2 elements are possible to be in a result
        # because of n//3, which makes it impossible for more than
        # two elements be greater than the third of the length of nums

        cand1 = None
        cand2 = None
        # None helps us avoid crashes, if there are fewer than 2 elements
        count1 = 0
        count2 = 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = count2 = 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1

        # verification
        n = len(nums)
        res = []
        if count1 > n // 3:
            res.append(cand1)
        if count2 > n // 3:
            res.append(cand2)
        return res
            
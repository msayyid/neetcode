from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:                      
        l, r = 0, len(people) - 1
        people.sort()
        count = 0
        while l <= r:
            if people[l] + people[r] > limit:
                count += 1
                r -= 1
            else:                
                r -= 1
                l += 1
                count += 1
        return count
    
# first sort 
# second, use two pointers, l and r
# if p of l + p of r > limit:
#       count += 1, r -= 1
# else:
# r -= 1, l += 1, count += 1
# return count 
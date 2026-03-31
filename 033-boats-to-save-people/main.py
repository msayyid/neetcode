from typing import List

# sorting + two pointers
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:                      
        l, r = 0, len(people) - 1
        count = 0
        people.sort()
        while l <= r:
            if people[l] + people[r] > limit:
                count += 1
                r -= 1
            else:
                count += 1
                l += 1
                r -= 1
        
        return count
    

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort people by weight so we can use two-pointer strategy
        people.sort()

        # l -> lightest person, r -> heaviest person
        l, r = 0, len(people) - 1

        # Count of boats used
        count = 0

        # Continue until all people are assigned to boats
        while l <= r:
            # Try to pair the lightest and heaviest person
            if people[l] + people[r] <= limit:
                # If they fit together, move both pointers
                l += 1

            # In both cases (paired or not), the heaviest person gets on a boat
            r -= 1

            # One boat is used in this iteration
            count += 1

        return count
    
# Always try to pair the heaviest with the lightest.
# If they can't pair, the heaviest must go alone.
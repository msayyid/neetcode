import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / speed)

            if total_time <= h:
                return speed
            
            speed += 1

        return speed


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_speed = right
        while left <= right:
            total_time = 0
            mid = (left + right) // 2

            for pile in piles:
                total_time += math.ceil(pile / mid)

            if total_time <= h:
                right = mid - 1
                min_speed = min(mid, min_speed)

            else:
                left = mid + 1

        return min_speed

            

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        min_speed = right
        while left <= right:
            mid = (left + right) // 2

            # now calculate the overall time
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)

            if total_time <= h:
                right = mid - 1
                min_speed = min(min_speed, mid)
            else:
                left = mid + 1

        return min_speed
    

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_speed = right
        while left <= right:
            total_time = 0
            mid = (left + right) // 2

            for pile in piles:
                total_time += math.ceil(pile / mid)

            if total_time <= h:
                right = mid - 1
                min_speed = mid

            else:
                left = mid + 1

        return min_speed

            
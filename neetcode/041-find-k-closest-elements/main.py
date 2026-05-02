from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1 # -1 because of the 0 indexed nature of arrays
        while r - l + 1 > k:
            left_dist = abs(x - arr[l])
            right_dist = abs(x - arr[r])
            if left_dist <= right_dist: # if left is closer to x or a tie
                # we move right pointer
                r -= 1
            else: # else if right dist is closer to x we do not need left as a starting point for us
                # so we move left
                l += 1
        return arr[l:r + 1]


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k # because we need room for the k elemtns if 
                         # r is a starting point

        while l < r:
            # pick a middle starting point to test
            mid = (l + r) // 2

            # we compare the first element of this window (arr[mid])
            # with the very next element after this window (arr[mid + k])

            if abs(arr[mid] - x) <= abs(arr[mid + k] - x): 
                # if the element at "mid" is closer to x (or it is a tie),
                # our best window cannot start any further to the right
                # so we bring the right boundary r to mid
                r = mid
            else:
                # if the element at mid + k is closer to x, it means
                # the current mid is a bad start. we should shift right
                l = mid + 1 # we move the left pointer to the next of mid and cut the current l and r in half
        
        # after the loop, l has found the best possible starting index
        # return k elements starting from that index
        return arr[l:l+k]


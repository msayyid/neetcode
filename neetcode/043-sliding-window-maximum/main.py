from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k - 1
        result = []
        while right < len(nums):
            max_element = max(nums[left:right + 1])
            result.append(max_element)
            left += 1
            right += 1

        return result

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k - 1
        result = []
        while right < len(nums):
            max_element = nums[left]
            for i in range(left, right + 1):
                max_element = max(max_element, nums[i])
            result.append(max_element)
            left += 1
            right += 1

        return result
    

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        q = deque() # we store the indices of values to ensure window is correct

        left = right = 0

        while right < len(nums):
            # q stores indices of possible max values for the current window
            # so we will be popping if the previous elements become useless
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # we append the next element, this is an element that could
            # potentially be the next max for a window
            q.append(right) # we need to be appending indices !!!!!!

            # we also need to make sure our left boundary is moving 
            # and make sure to remove the max elements that are no longer relevant
            # or not in our window
            if left > q[0]: # if left boundary is greater than the index of the first element in the q, we popleft, to make sure, this element does not become max for other windwos, since the first elmeent in the q is the current max 
                q.popleft()
            # now we need to update the result
            # first check if we have the valid window
            if (right + 1) >= k:
                output.append(nums[q[0]]) # q[0] has the largest value's index
                left += 1
            right += 1

        
        return output
    

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        q = deque()
        left = right = 0

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            if left > q[0]:
                q.popleft()

            if right + 1 >= k:
                result.append(nums[q[0]])
                left += 1

            right += 1

        return result
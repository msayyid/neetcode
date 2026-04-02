from typing import List

# brute force On^2 time and O1 space
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        water = 0
        for i in range(n):
            left_max = height[i]
            right_max = height[i]
            for j in range(i):
                left_max = max(left_max, height[j])
            for j in range(i + 1, n):
                right_max = max(right_max, height[j])
            water += min(left_max, right_max) - height[i]
        return water
    

# second approach with prefixes On time On space
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = height[0] # because there's nothing before 0's index
        for i in range(n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        return water
    
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        return res
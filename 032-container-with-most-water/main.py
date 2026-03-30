from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        # loop through each line as the left boundary
        for i in range(len(heights)):
            # start j from i + 1 to:
            # 1. avoid checking the same index (i != j)
            # 2. avoid duplicate pairs like (i, j) and (j, i)
            # since they produce the same area
            for j in range(i + 1, len(heights)):
                area = (min(heights[i], heights[j])) * (j - i)
                if area > max_area:
                    max_area = area
        return max_area

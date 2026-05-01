from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        my_array = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                my_array.append(matrix[i][j])

        left = 0
        right = len(my_array) - 1
        while left <= right:
            mid = (left + right) // 2
            if my_array[mid] == target:
                return True
            elif my_array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False # stupid brute force
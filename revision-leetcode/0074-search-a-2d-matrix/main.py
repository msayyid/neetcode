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
    
# goodder brute force
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False
    
# one pass optimal binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n * m - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return False

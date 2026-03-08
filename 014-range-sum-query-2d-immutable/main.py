from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])

        # create a (rows+1) x (cols+1) matrix filled with 0s
        # the extra row and column of zeros act as padding to prevent
        # out of bounds errors when the formula needs to look at row1-1 or col1-1
        self.sumMat = [[0] * (cols + 1) for r in range(rows + 1)]

        # build the 2D prefix sum matrix
        # sumMat[i][j] = sum of all elements from (0,0) to (i-1, j-1) in original matrix
        for r in range(rows):
            prefix = 0  # running row sum, resets to 0 for each new row
            for c in range(cols):
                prefix += matrix[r][c]          # accumulate current row sum up to col c
                above = self.sumMat[r][c + 1]   # sum of everything above current cell
                                                 # uses c+1 (not c) because of the +1 shift from padding
                self.sumMat[r + 1][c + 1] = prefix + above  # store rectangle sum from (0,0) to (r,c)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # all indices are +1 shifted to map original matrix coords to sumMat coords

        bottomRight = self.sumMat[row2 + 1][col2 + 1]  # sum of entire rectangle from (0,0) to (row2, col2)
        above = self.sumMat[row1][col2 + 1]             # sum of rectangle above our region (to be removed)
        left = self.sumMat[row2 + 1][col1]              # sum of rectangle left of our region (to be removed)
        topLeft = self.sumMat[row1][col1]               # top-left corner, subtracted twice so we add it back once

        # inclusion-exclusion: remove above and left, add back topLeft which was removed twice
        return bottomRight - above - left + topLeft


# Time:  O(m*n) to build sumMat — must read every cell at least once, paid once regardless of query count
#        O(1)   per sumRegion call — just arithmetic on 4 precomputed values
# Space: O(m*n) for sumMat


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
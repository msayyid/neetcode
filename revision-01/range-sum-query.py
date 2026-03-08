from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        row = len(matrix)
        col = len(matrix[0])
        # then create a r + 1 and c + 1 matrix to avoid edge cases
        self.bigger_matrix = [[0] * (col + 1) for r in range(row +1 )]
        # now we have a bigger matrix + 1 in r and c filled with 0s 

        # now we set the actual values for the bigger matrix. the idea:
        # bottom right corner is gonna have a sum of that rectangle 
        # starting from (0, 0)

        for r in range(row):
            prefix = 0
            for c in range(col):
                # calculate the top and prefix and place it in the bigger matrix
                prefix += matrix[r][c]
                # we calculate everything above this current matrix from bigger matrix
                # because it has the sum of all the values up to it
                above = self.bigger_matrix[r][c+1]
                self.bigger_matrix[r+1][c+1] = prefix + above # now this place contains the area
                # from 0, 0 to this place, in the first iteration it contains the very first 
                # element of the very first value in original matrix
                # making it our first sum of area of (0, 0) to (0, 0) in this case
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # now we have our bigger matrix ready
        # we just need to calculate the area for the given
        # rectangle points
        the_full_area =  self.bigger_matrix[row2+1][col2+1]
        the_left = self.bigger_matrix[row2+1][col1]
        the_top = self.bigger_matrix[row1][col2+1]
        the_diagonal = self.bigger_matrix[row1][col1]
        return the_full_area - the_left - the_top + the_diagonal
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
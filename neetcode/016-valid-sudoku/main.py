from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Set to track numbers seen in the current row
        row = set()

        # Set to track numbers seen in the current column
        column = set()

        # Dictionary to store sets for each 3x3 box
        # key -> (box_row, box_col)
        boxes = dict()

        # Iterate through rows
        for i in range(len(board)):

            # Iterate through columns
            for j in range(len(board[i])):

                # ----- ROW CHECK -----
                # If number already exists in row -> invalid sudoku
                if board[i][j] in row:
                    return False

                # Ignore empty cells
                if board[i][j] != ".":
                    row.add(board[i][j])


                # ----- COLUMN CHECK -----
                # board[j][i] flips indices to read column values
                if board[j][i] in column:
                    return False

                if board[j][i] != ".":
                    column.add(board[j][i])


                # ----- 3x3 BOX CHECK -----
                # Determine which 3x3 box the cell belongs to
                loc = (i//3, j//3)

                # Get the set for this box (or empty set if not created yet)
                check_set = boxes.get(loc, set())

                # If value already exists in this box -> invalid sudoku
                if board[i][j] in check_set:
                    return False

                # Add number to this box set
                if board[i][j] != ".":
                    check_set.add(board[i][j])
                    boxes[loc] = check_set

            # Reset row and column sets for the next iteration
            row = set()
            column = set()
        
        return True
        
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Track numbers seen in the current row
        row = set()

        # Track numbers seen in the current column
        column = set()

        # Store numbers for each 3x3 box
        boxes = dict()

        # Sudoku board is always 9x9
        for i in range(9):

            for j in range(9):

                # Identify which 3x3 box the cell belongs to
                loc = (i//3, j//3)

                # Get the set for this box
                check_set = boxes.get(loc, set())

                # Check three conditions:
                # 1. number already exists in row
                # 2. number already exists in column
                # 3. number already exists in the 3x3 box
                if (board[i][j] in row or 
                    board[j][i] in column or 
                    board[i][j] in check_set):
                    return False

                # Add value to row set if not empty
                if board[i][j] != ".":
                    row.add(board[i][j])

                # Add value to column set if not empty
                if board[j][i] != ".":
                    column.add(board[j][i])

                # Add value to the corresponding 3x3 box
                if board[i][j] != ".":
                    check_set.add(board[i][j])
                    boxes[loc] = check_set

            # Reset row and column tracking for next row
            row = set()
            column = set()
        
        return True

            
        
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Dictionary where each row index maps to a set of numbers
        row = defaultdict(set)

        # Dictionary where each column index maps to a set of numbers
        column = defaultdict(set)

        # Dictionary where each (box_row, box_col) maps to numbers in that box
        boxes = defaultdict(set)

        # Loop through every cell in the board
        for i in range(9):
            for j in range(9):

                # Skip empty cells
                if board[i][j] == ".":
                    continue

                # Check if number already exists in:
                # - the same row
                # - the same column
                # - the same 3x3 box
                if (board[i][j] in row[i] or
                    board[i][j] in column[j] or
                    board[i][j] in boxes[(i//3, j//3)]):
                    return False

                # Record the number in row tracker
                row[i].add(board[i][j])

                # Record the number in column tracker
                column[j].add(board[i][j])

                # Record the number in the corresponding 3x3 box
                boxes[(i//3, j//3)].add(board[i][j])

        return True
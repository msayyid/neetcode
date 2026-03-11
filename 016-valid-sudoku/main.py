class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        column = set()
        boxes = dict()
        for i in range(len(board)):
            # row = set()
            for j in range(len(board[i])):
                if board[i][j] in row:
                    return False
                if board[i][j] != ".":
                    row.add(board[i][j])

                # column
                if board[j][i] in column:
                    return False
                if board[j][i] != ".":
                    column.add(board[j][i])

                # squares
                loc = (i//3, j//3)
                check_set = boxes.get(loc, set())
                if board[i][j] in check_set:
                    return False
                if board[i][j] != ".":
                    check_set.add(board[i][j])
                    boxes[loc] = check_set

            row = set()
            column = set()
        
        return True

            
        
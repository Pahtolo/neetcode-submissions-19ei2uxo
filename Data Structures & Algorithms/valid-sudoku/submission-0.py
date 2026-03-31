class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True

        top_left = []
        top_middle = []
        top_right = []
        middle_left = []
        middle_middle = []
        middle_right = []
        bottom_left = []
        bottom_middle = []
        bottom_right = []
        #checks columns and rows
        for i in range(len(board)):
            row = []
            column = []
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    target_box = None
                    if i < 3:
                        if j < 3: target_box = top_left
                        elif j < 6: target_box = top_middle
                        else: target_box = top_right
                    elif i < 6:
                        if j < 3: target_box = middle_left
                        elif j < 6: target_box = middle_middle
                        else: target_box = middle_right
                    else:
                        if j < 3: target_box = bottom_left
                        elif j < 6: target_box = bottom_middle
                        else: target_box = bottom_right
                    
                    if board[i][j] in target_box:
                        return False
                    target_box.append(board[i][j])

                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j])
                
                if board[j][i] != '.':
                    if board[j][i] in column:
                        return False
                    column.append(board[j][i])

        return valid
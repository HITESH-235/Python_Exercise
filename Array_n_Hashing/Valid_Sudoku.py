# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# LEETCODE link: https://leetcode.com/problems/valid-sudoku/submissions/1720037217/

def valid_sudoku(board):
    # checking rows and columns at once
    for row in range(9):
        unique_row_nums = set()
        unique_col_nums = set()

        for col in range(9):
            cur_row_num = board[row][col]
            cur_col_num = board[col][row]

            if cur_row_num in unique_row_nums or cur_col_num in unique_col_nums:
                return False
            if cur_row_num != ".":
                unique_row_nums.add(cur_row_num)
            if cur_col_num != ".":
                unique_col_nums.add(cur_col_num)

    # check each 3x3 box:
    i = 0
    for i in range(0,9,3):
        for j in range(0,9,3):
            unique_nums = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    cur = board[row][col]

                    if cur in unique_nums:
                        return False
                    if cur != ".":
                        unique_nums.add(cur)
    return True
            
true_sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
false_sudoku_board = [       
    [".", ".", ".", ".", "5", ".", ".", "3", "."],
    [".", "4", ".", "2", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", "9", "3"],
    [".", "2", ".", "9", ".", ".", "6", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", "9", "."]]

print(valid_sudoku(true_sudoku_board))
print(valid_sudoku(false_sudoku_board))
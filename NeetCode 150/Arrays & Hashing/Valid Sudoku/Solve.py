def check_duplicate(board):
    for each_list in board:
        digits = ["1","2","3","4","5","6","7","8","9"]
        
        for each_digit in each_list:
            if each_digit == ".":
                continue
            if each_digit in digits:
                digits.remove(each_digit)
            else:
                return True
    
def get_subgrids(board):
    subgrids = []
    for i in range(0, 9, 3):  # Iterate over each block of 3 rows
        for j in range(0, 9, 3):  # Iterate over each block of 3 columns
            subgrid = []
            for k in range(3):  # Iterate over the 3 rows in the 3x3 block
                subgrid.extend(board[i + k][j:j + 3])  # Extract 3 columns from the current row
            subgrids.append(subgrid)
    return subgrids

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        if check_duplicate(board): # Checking each row (1st condition)
            return False

        transposed_board = list(map(list, zip(*board))) # converting column to row for ease of use
        if check_duplicate(transposed_board): # Checking each column (2nd Condition)
            return False
        
        sub_board = get_subgrids(board) # Get the 3x3 sub-grids as list
        if check_duplicate(sub_board): # Checking each 3x3 sub-grids (3rd Condition)
            return False
        
        return True
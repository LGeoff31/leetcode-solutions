class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = []

        # Iterate through the Sudoku board.
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                # Check if the element is not '.' (empty cell).
                if ele != '.':
                    # Check for violations in the current row, column, and subgrid.
                    r += [(i, ele), (ele, j), (i // 3, j // 3, ele)]
        print(r)
        # Return True if there are no violations, i.e., the length of the list is equal to the length of the set.
        return len(r) == len(set(r))
        
        
from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows, cols = len(board), len(board[0])

        while True:
            crush = set()

            # Mark horizontal candies
            for r in range(rows):
                for c in range(cols - 2):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r][c+1]) == abs(board[r][c+2]):
                        crush.update({(r, c), (r, c+1), (r, c+2)})

            # Mark vertical candies
            for r in range(rows - 2):
                for c in range(cols):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r+1][c]) == abs(board[r+2][c]):
                        crush.update({(r, c), (r+1, c), (r+2, c)})

            # If no crushes, we're done
            if not crush:
                return board

            # Crush marked candies
            for r, c in crush:
                board[r][c] = 0

            # Apply gravity
            for c in range(cols):
                write_row = rows - 1
                for r in reversed(range(rows)):
                    if board[r][c] != 0:
                        board[write_row][c] = board[r][c]
                        write_row -= 1
                for r in range(write_row + 1):
                    board[r][c] = 0

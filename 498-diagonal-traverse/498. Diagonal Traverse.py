from typing import List

class Solution:
    def findDiagonalOrder(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        res = []

        up = True
        up_start = (0, 0)       # start of the next upward diagonal
        down_start = (0, 1)     # start of the next downward diagonal (right of (0,0) if exists)

        while len(res) < rows * cols:
            if up:
                r, c = up_start
                # traverse up-right
                while 0 <= r < rows and 0 <= c < cols:
                    res.append(grid[r][c])
                    r -= 1
                    c += 1
                # step back to last valid cell
                r += 1
                c -= 1
                # choose next start for DOWN:
                # if we ended at the right edge, go down one row;
                # otherwise (we ended at the top), go right one col
                if c == cols - 1:
                    down_start = (r + 1, c) if r + 1 < rows else (rows - 1, cols - 1)
                else:
                    down_start = (r, c + 1)
            else:
                r, c = down_start
                # traverse down-left
                while 0 <= r < rows and 0 <= c < cols:
                    res.append(grid[r][c])
                    r += 1
                    c -= 1
                # step back to last valid cell
                r -= 1
                c += 1
                # choose next start for UP:
                # if we ended at the bottom edge, go right one col;
                # otherwise (we ended at the left), go down one row
                if r == rows - 1 and c + 1 < cols:
                    up_start = (r, c + 1)
                else:
                    up_start = (r + 1, c) if r + 1 < rows else (rows - 1, cols - 1)

            up = not up

        return res

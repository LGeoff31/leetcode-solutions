class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 1
        for r in range(rows):
            for c in range(cols):
                for delta in range(1,51):
                    if not (0 <= r+delta < rows and 0 <= c+delta < cols):
                        continue

                    square = []
                    for dr in range(r, r+delta+1):
                        square_row = []
                        for dc in range(c,c+delta+1):
                            square_row.append(grid[dr][dc])
                        square.append(square_row)
                    rowSum = [sum(row) for row in square]
                    colSum = [sum(col) for col in zip(*square)]
                    diagonal1 = sum(square[dr][dr] for dr in range(len(square)))
                    diagonal2 = sum(square[dr][delta - dr] for dr in range(len(square)))    
                    rowSum.sort()
                    colSum.sort()
                    # print(rowSum, colSum, r, c, delta, diagonal1, diagonal2)
                    if rowSum[0] == rowSum[-1] == colSum[0] == colSum[-1] == diagonal1 == diagonal2:
                        res = max(res, delta + 1)
        return res
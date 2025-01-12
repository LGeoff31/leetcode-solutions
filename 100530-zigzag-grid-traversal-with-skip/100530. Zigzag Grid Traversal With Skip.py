class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(grid), len(grid[0])
        take = True
        increasing = True
        for r in range(rows):
            if increasing:
                for c in range(cols):
                    if take:
                        res.append(grid[r][c])
                    take = not take
            else:
                for c in range(cols - 1, -1, -1):
                    if take:
                        res.append(grid[r][c])
                    take = not take
            increasing = not increasing
        return res
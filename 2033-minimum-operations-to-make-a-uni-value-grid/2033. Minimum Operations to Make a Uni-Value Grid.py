class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        rows, cols = len(grid), len(grid[0])
        a = [grid[r][c] for r in range(rows) for c in range(cols)]
        val = sorted(a)[len(a) // 2]

        res = 0
        for r in range(rows):
            for c in range(cols):
                diff = abs(grid[r][c] - val)
                if diff % x != 0:
                    return -1
                res += diff // x
        return res
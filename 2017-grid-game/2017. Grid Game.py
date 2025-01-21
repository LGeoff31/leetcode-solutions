class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        res = float("inf")
        n = len(grid[0])
        totalSumFirstRow = sum(grid[0])
        prefix1 = list(accumulate(grid[0]))
        prefix2 = list(accumulate(grid[1]))
        for i in range(n):
            res = min(res, max(prefix2[i] - grid[1][i], totalSumFirstRow - prefix1[i]))
        return res
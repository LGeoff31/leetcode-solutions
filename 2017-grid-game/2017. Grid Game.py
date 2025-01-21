class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        res = float("inf")
        totalSumFirst = sum(grid[0])
        prefix1 = list(accumulate(grid[0]))
        prefix2 = list(accumulate(grid[1]))
        n = len(grid[0])
        for i in range(n):
            res = min(res, max(prefix2[i] - grid[1][i], totalSumFirst - prefix1[i]))

        return res
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        rows, cols = len(grid), len(grid[0])

        @cache
        def dfs(r,c, currSum):
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if r == rows - 1 and c == cols - 1:
                currSum += grid[r][c]
                return currSum % k == 0

            return (dfs(r+1, c, (currSum + grid[r][c]) % k) + dfs(r, c+1, (currSum + grid[r][c]) % k)) % MOD
        res = int(dfs(0, 0, 0)) % MOD
        dfs.cache_clear()
        return res
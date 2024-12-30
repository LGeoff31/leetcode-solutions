class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(curr):
            if curr == n:
                return 1
            if curr > n:
                return 0
            return dfs(curr + 1) + dfs(curr + 2)
        return dfs(0)
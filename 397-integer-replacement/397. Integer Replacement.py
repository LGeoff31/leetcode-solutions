class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def dfs(n):
            if n == 1:
                return 0

            if n % 2 == 0:
                return 1 + dfs(n // 2)
            else:
                return 1 + min(dfs(n+1), dfs(n-1))
        return dfs(n)
class Solution:
    def minCost(self, n: int) -> int:
        @cache
        def dfs(n):
            if n <= 1:
                return 0
            return (n - n//2) * (n//2) + dfs(n//2) + dfs(n- n//2)
        
        return dfs(n)
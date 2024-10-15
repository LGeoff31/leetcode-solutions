class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache
        def dfs(i): # 
            if i == 1:
                return k
            if i == 2:
                return k * k
            
            return (k-1) * dfs(i-1) + (k-1) * dfs(i-2)
        return dfs(n)
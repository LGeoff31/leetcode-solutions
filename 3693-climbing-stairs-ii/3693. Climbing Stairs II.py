class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def dfs(i):
            if i == n:
                return 0
            
            res = 1e9
            if i + 1 <= n:
                res = min(res, dfs(i+1) + (costs[i] + 1))
            if i + 2 <= n:
                res = min(res, dfs(i+2) + (costs[i+1] + 4))
            if i + 3 <= n:
                res = min(res, dfs(i+3) + (costs[i+2] + 9))
            return res
        
        return dfs(0)

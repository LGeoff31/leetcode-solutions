class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        @cache
        def dfs(idx, prevColor, lastColor):
            if idx >= n // 2:
                return 0
            
            res = 1e20

            for i in range(3): # from left side
                for j in range(3): # from right side
                    if i != prevColor and i != j and j != lastColor:
                        res = min(res, cost[idx][i] + cost[n-idx-1][j] + dfs(idx+1, i, j))
            return res
        return dfs(0, -1, -1)
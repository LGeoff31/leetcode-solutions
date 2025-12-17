class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        @cache
        def dfs(i, transactions, pos):
            if transactions > k:
                return -1e18
            res = 0 
            # BASE CASES
            if i == len(prices):
                return 0 if pos == 0 else -1e18


            res = dfs(i+1, transactions, pos)
            if pos == 1:
                res = max(res, prices[i] + dfs(i+1, transactions + 1, 0))
            elif pos == -1:
                res = max(res, -prices[i] + dfs(i+1, transactions + 1, 0))
            else:
                res = max(res, -prices[i] + dfs(i+1, transactions, 1))
                res = max(res, prices[i] + dfs(i+1, transactions, -1))

            return res
        res = dfs(0, 0, 0)
        dfs.cache_clear()
        return res
        

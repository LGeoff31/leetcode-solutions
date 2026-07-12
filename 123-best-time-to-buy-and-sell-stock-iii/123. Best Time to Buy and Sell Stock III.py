class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        At each index, you can either BUY (if not in transaction and < 2), SELL (if in transaction), NOTHING
        def dfs(i, transactions_left, free'd)
        """
        @cache
        def dfs(i, transactions_left, ready_to_buy):
            if i == len(prices):
                return 0
            
            res = 0
            if ready_to_buy:
                if transactions_left > 0:
                    res = max(res, dfs(i+1, transactions_left-1, not ready_to_buy) - prices[i])
            else:
                res = max(res, dfs(i+1, transactions_left, not ready_to_buy) + prices[i])
            res = max(res, dfs(i+1, transactions_left, ready_to_buy))
            return res
        return dfs(0, 2, True)
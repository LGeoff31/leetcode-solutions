class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        At each index, you can either BUY (if not in transaction and < 2), SELL (if in transaction), NOTHING
        def dfs(i, transactions_left, free'd)
        dp[i][transactions_left][ready_to_buy] = max amount achieved at index i with transactions_left and ready_to_buy booleean
        """

        n = len(prices)
        dp = [[[0, 0] for _ in range(3)] for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for t in range(3):
                for r in range(2):
                    res = 0
                    if r:
                        if t > 0:
                            res = max(res, dp[i+1][t-1][0] - prices[i])
                    else:
                        res = max(res, dp[i+1][t][1] + prices[i])
                    res = max(res, dp[i+1][t][r])
                    dp[i][t][r] = res

        return dp[0][2][1]
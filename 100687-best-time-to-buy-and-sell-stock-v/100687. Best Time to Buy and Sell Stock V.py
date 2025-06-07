class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # dp[i][k][(0,1,2)] -> maximum profit at indicies i, when you take the action (0,1,2) -> (buy, sell, nothing)
        # dp[i][k][0] = max(dp[i-1][k-1][1])
        # dp[i] = max profit index i 
        dp = [0] * len(prices)
        for i in range(k):
            local_dp = [0] * len(prices)
            buy, sell = -prices[0], prices[0]
            for j in range(1, len(prices)):
                buy = max(buy, dp[j-1] - prices[j])
                sell = max(sell, dp[j-1] + prices[j])

                # no transactions, buy, sell
                local_dp[j] = max(local_dp[j-1], buy + prices[j], sell - prices[j])
            dp = local_dp
        return dp[-1]
        # def dfs(i, k):
        #     for idx in range(i, len(prices)):
        #         # At this indicies you can buy or sell
        #         dfs(i+1 )
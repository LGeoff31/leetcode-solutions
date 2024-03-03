class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0]

        for i in range(1, len(prices)):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i])
            sell[i] = max(sell[i-1], prices[i] + buy[i-1] - fee)
        return sell[-1]
        
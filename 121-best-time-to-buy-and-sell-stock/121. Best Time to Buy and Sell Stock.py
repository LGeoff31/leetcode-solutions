class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
                right += 1
            else:
                max_profit = max(max_profit, profit)
                right += 1
        return max_profit


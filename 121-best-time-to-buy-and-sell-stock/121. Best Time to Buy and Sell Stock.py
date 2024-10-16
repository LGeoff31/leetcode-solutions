class Solution:
    def noProfit(self, prices):
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                return False
        return True

    def maxProfit(self, prices: List[int]) -> int:
        if self.noProfit(prices):
            return 0 #O(N) => funciton scans through prices
        max_profit = -99999
        #kandaine algorithm
        l, r = 0, 1
        while r < len(prices):
            if prices[r] - prices[l] < 0: #negative profit
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1
        return max_profit


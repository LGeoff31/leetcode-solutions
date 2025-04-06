class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1e9
        res = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            res = max(res, prices[i] - min_price)


        return res
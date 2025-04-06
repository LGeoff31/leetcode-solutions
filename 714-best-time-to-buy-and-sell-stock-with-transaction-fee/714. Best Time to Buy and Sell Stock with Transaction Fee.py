class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res = 0
        hold = -prices[0]

        for i in range(1, len(prices)):
            res = max(res, prices[i] + hold - fee) # 5
            hold = max(hold, res - prices[i]) # 1
        return res
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minimum = 1e9

        for i in range(len(prices)):
            res = max(res, prices[i] - minimum)
            minimum = min(minimum, prices[i])
 
        return res
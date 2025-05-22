class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = -1e9
        smallest_so_far = 1e9
        for i in range(len(prices)):
            smallest_so_far = min(smallest_so_far, prices[i])
            res = max(res, prices[i] - smallest_so_far)
        return res
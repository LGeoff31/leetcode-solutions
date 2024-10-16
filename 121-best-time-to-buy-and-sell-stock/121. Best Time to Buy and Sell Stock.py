class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global_max = 0
        left, right = 0, 1
        
        while right < len(prices):
            if prices[right] - prices[left]  > 0:
                curr_max = prices[right] - prices[left]
                global_max = max(global_max, curr_max)
            else:
                left = right
            right += 1
        return global_max            




        
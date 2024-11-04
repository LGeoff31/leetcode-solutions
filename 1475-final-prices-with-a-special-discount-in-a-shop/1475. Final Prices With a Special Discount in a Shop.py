class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        prefix = [1e9] * len(prices)
        prefix[-1] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            prefix[i] = min(prefix[i+1], prices[i])
        ans = []
        for i in range(len(prices)):
            found = False
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    ans.append(prices[i] - prices[j])
                    found = True
                    break
            if not found:
                ans.append(prices[i])
                
        return ans
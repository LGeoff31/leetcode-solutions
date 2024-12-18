class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            ans.append(prices[i] - discount)
        return ans
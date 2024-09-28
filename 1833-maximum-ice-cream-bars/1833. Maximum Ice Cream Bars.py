class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        while i < len(costs) and coins > 0:
            coins -= costs[i]
            if coins < 0: break
            i += 1
        return i
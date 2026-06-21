class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        curr = 0
        for c in costs:
            if curr + c <= coins:
                res += 1
                curr += c
        return res
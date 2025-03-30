class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res = [0] * len(cost)
        for i in range(len(cost)):
            res[i] = min(cost[:i+1])
        return res
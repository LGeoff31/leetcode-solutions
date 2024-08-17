class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        cost = values[0] - 1
        for i in range(1, len(values)):
            res = max(res, cost + values[i])
            cost = max(cost-1, values[i] - 1)
        return res

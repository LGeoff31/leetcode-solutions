class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = values[1] + values[0] - 1
        prev = max(values[0]-1, values[1])
        for i in range(2, len(values)):
            prev = max(prev - 1, values[i-1] - 1)
            res = max(res, prev + values[i])
        return res
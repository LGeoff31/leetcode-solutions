class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minElem, maxElem = 1e9, -1e9
        minElem = min(minElem, arrays[0][0])
        maxElem = max(maxElem, arrays[0][-1])
        res = -1e9
        for i in range(1, len(arrays)):
            res = max(res, arrays[i][-1] - minElem, maxElem - arrays[i][0])
            minElem = min(minElem, arrays[i][0])
            maxElem = max(maxElem, arrays[i][-1])
        return res


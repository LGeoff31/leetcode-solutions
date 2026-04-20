class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        for i in range(len(colors)):
            for j in range(i+1, len(colors)):
                if colors[j] != colors[i]:
                    res = max(res, j-i)
        return res
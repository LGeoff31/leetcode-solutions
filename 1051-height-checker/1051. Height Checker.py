class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a = sorted(heights)
        res = 0
        for i in range(len(heights)):
            res += heights[i] != a[i]
        return res
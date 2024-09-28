class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        n = len(colors)
        l, r = 0, len(colors) - 1

        while l <= r:
            if colors[l] != colors[-1]:
                res = max(res, n-l-1)
            if colors[r] != colors[0]:
                res = max(res, r)
            
            l += 1
            r -= 1
        return res
        
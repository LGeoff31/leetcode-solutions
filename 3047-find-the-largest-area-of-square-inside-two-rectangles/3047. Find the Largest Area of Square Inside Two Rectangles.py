class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        res = 0
        n = len(bottomLeft)
        def maxArea(i,j):
            a,b = bottomLeft[i]
            c,d = topRight[i]

            e,f = bottomLeft[j]
            g,h = topRight[j]

            height_overlap = max(0, min(d, h) - max(b, f))
            width_overlap = max(0, min(c, g) - max(a, e))


            return min(height_overlap, width_overlap) ** 2

        for i in range(n):
            for j in range(i+1, n):
                res = max(res, maxArea(i,j))

        return res
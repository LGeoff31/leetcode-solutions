class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        res = 0
        def heron(s1, s2, s3):
            semi_p = (s1+s2+s3) / 2
            if semi_p * (semi_p - s1) * (semi_p - s2) * (semi_p - s3) >= 0:
                return sqrt(semi_p * (semi_p - s1) * (semi_p - s2) * (semi_p - s3))
            return 0
        def dist(p1, p2):
            return sqrt(abs(p1[0]-p2[0]) ** 2 +  abs(p1[1]-p2[1]) ** 2)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    a,b,c = points[i], points[j], points[k]
                    res = max(res, heron(dist(a,b), dist(a,c), dist(b,c)))
        return res 

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        def slope(pt1, pt2):
            x1, y1 = pt1
            x2, y2 = pt2

            if x2 == x1:
                # This would make a vertical line 
                return 1e5
            return (y2 - y1) / (x2 - x1)
        
       
        res = 1
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                s = slope(points[i], points[j])
                cnt = 1
                for point in points:
                    if point != points[i] and slope(points[i], point) == s:
                        cnt += 1
                res = max(res, cnt)

        return res
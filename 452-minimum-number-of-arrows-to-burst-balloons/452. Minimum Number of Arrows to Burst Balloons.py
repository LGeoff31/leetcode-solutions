class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 0
        idx = 1
        min_x = points[0][1]
        while idx < len(points):
            start, end = points[idx]
            if start > min_x:
                res += 1
                min_x = end
            else:
                min_x = min(min_x, end)
            idx += 1
        return res+1
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        dic = {(x,y) for x,y in points}
        res = 0
        def point_inside(x1, y1, x2, y2, x3, y3, x4, y4):
            # Calculate the bounding rectangle
            x_min = min(x1, x3)
            x_max = max(x1, x3)
            y_min = min(y1, y3)
            y_max = max(y1, y3)
            corners = {(x1, y1), (x2, y2), (x3, y3), (x4, y4)}
            
            for x, y in points:
                # Check if point lies within the rectangle
                if x_min <= x <= x_max and y_min <= y <= y_max and (x,y) not in corners:
                    return True  # At least one point lies within the rectangle
            
            return False  # No point lies within the rectangle 
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2: continue
                point3 = [x2, y1]
                point4 = [x1, y2]
                if tuple(point3) in dic and tuple(point4) in dic:
                    if not point_inside(x1,y1, point3[0], point3[1], x2,y2, point4[0], point4[1]):
                        res = max(res, abs(x1-x2)*abs(y1-y2))
        return res if res > 0 else -1

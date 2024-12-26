class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # No rectagnels can overlap
        # There must be no empty region between the rectangles
        # They must 
        corners = set()
        area = 0

        for x, y, X, Y in rectangles:
            corners ^= {(x,y), (x,Y), (X, y), (X, Y)}
            area += abs(y-Y) * abs(x-X)
        if len(corners) != 4: return False
        x,y = min(corners, key=lambda x : x[0] + x[1])
        X,Y = max(corners, key=lambda x : x[0] + x[1])
        return area == (x-X) * (y-Y)
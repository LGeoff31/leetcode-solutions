class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        create y=mx+b, using the two centere's
        see the intersection of that line and the rectnagle, that point will be the closest point to the circle, return distance <= radius
        y-y1 = m(x-x1)
        """
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        return abs(xCenter-closest_x) ** 2 + abs(yCenter-closest_y) ** 2 <= radius ** 2
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x_dist = min(ax2,bx2) - max(ax1, bx1)
        y_dist = min(ay2,by2) - max(ay1, by1)
        if x_dist > 0 and y_dist > 0:

            return abs(ax1-ax2) * abs(ay1-ay2) + abs(bx1-bx2) * abs(by1-by2) - x_dist * y_dist
        return abs(ax1-ax2) * abs(ay1-ay2) + abs(bx1-bx2) * abs(by1-by2)
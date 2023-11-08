class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        x_dist = abs(sx-fx)
        y_dist = abs(sy-fy)
        if x_dist == 0 and y_dist == 0 and t == 1:
            return False
        min_nums = min(x_dist, y_dist)
        x_dist -= min_nums
        y_dist -= min_nums
        t -= min_nums

        a = max(x_dist, y_dist)
        if t >= a:
            return True
        return False

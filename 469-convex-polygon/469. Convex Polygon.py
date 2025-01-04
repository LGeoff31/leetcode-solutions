class Solution:
    def computeAngleABPerp_AC(self, A, B, C) -> float:
        AB = (B[0] - A[0], B[1] - A[1]) # line from point A to B
        AB_perp = (AB[1], -AB[0]) # rotate line 90 degrees
        AC = (C[0] - A[0], C[1] - A[1]) # line from point A to C
        return AB_perp[0] * AC[0] + AB_perp[1] * AC[1] # dot product for angle between AC and line perpendicular to AB, sign indicates on which side of AB line C is

    def isConvex(self, points: List[List[int]]) -> bool:
        n = len(points)
        correct_sign = None
        for i in range(0, n):
            angle = self.computeAngleABPerp_AC(points[i], points[(i + 1) % n], points[(i + 2) % n])
            if angle == 0.0: # 3 colinear vertices, still convex
                continue
            if correct_sign is None: # correct sign depends on whether points are given clockwise or counterclockwise, discover it as we go
                correct_sign = angle > 0
            elif correct_sign != (angle > 0): # all points must lie on the same side of the line formed by the 2 preceding vertices
                return False
        return True
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        for r in range(1, len(points)):
            right = [0] * cols
            right[-1] = points[r-1][-1]
            for c in range(cols-2, -1, -1):
                right[c] = max(right[c+1] - 1, points[r-1][c])
            left = points[r-1][0]
            points[r][0] = max(left, right[0]) + points[r][0]
            for c in range(1, cols):
                left = max(left - 1, points[r-1][c])
                points[r][c] = max(left, right[c]) + points[r][c]
        return max(points[-1])

        
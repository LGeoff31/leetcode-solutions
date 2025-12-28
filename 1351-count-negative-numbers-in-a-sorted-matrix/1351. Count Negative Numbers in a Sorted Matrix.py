class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(c < 0 for row in grid for c in row)
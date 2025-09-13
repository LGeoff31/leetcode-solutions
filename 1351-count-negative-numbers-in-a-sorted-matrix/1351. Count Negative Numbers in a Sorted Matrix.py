class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(n < 0 for n in [b for x in grid for b in x])
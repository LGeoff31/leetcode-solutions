class Solution:
    def coloredCells(self, n: int) -> int:
        # 1 -> 1  (1 boundary)
        # 2 -> 5  (4 boundary)
        # 3 -> 13 (8 boundary)
        # 4 -> 25 (12 boundary)

        if n == 1: return 1

        return self.coloredCells(n-1) + 4 * (n-1)
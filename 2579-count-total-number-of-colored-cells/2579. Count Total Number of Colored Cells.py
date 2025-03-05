class Solution:
    def coloredCells(self, n: int) -> int:
        # 1 -> 1  (1 boundary)
        # 2 -> 5  (4 boundary)
        # 3 -> 13 (8 boundary)
        # 4 -> 25 (12 boundary)

        # 1, 1+4, 1+4+8, 1+4+8+12 (3 -> 4-1) 1 + 4(1+2+3)

        # 1 + 4(1+2) 2(3)//2

        if n == 1: return 1

        return 1 + 4 * (((n-1) * (n)) // 2)

        # 1+2+3 -> 
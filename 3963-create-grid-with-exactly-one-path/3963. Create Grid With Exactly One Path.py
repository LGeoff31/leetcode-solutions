class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = [["#"] * n for _ in range(m)]
        print(res)
        # First col
        for r in range(m):
            res[r][0] = '.'

        # Last row
        for c in range(n):
            res[-1][c] = '.'

        a = []
        for row in range(len(res)):
            a.append("".join(res[row]))
        return a
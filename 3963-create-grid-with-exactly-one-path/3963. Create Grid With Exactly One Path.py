class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        lst = [["#"] * n for _ in range(m)]

        for r in range(m):
            lst[r][0] = "."
        for c in range(n):
            lst[-1][c] = "."
        
        return ["".join(lst[r]) for r in range(len(lst))]

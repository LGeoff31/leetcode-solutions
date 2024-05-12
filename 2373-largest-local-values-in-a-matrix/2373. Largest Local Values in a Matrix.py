class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        res = [[0] * (n-2) for _ in range(n-2)]
        directions = (-1, 0, 1)
        for r in range(1, n-1):
            for c in range(1, n-1):
                val = 0
                for dr in directions:
                    for dc in directions:
                        val = max(val, grid[r+dr][c+dc]) 
                res[r-1][c-1] = val
        return res
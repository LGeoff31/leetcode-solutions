class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2+1):
                grid[r][c1] += 1
                if c2+1 < len(grid[0]): grid[r][c2+1]-=1
        print(grid)
        for r in range(len(grid)):
            for c in range(1, len(grid[0])):
                grid[r][c] = grid[r][c] + grid[r][c-1]
        return grid
        
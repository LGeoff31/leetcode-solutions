class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        count = 0
        direction = [(0,1), (0,-1), (1,0), (-1, 0)]
        def dfs(r,c):
            visited.add((r,c))
            if 0 <= r < rows and 0 <= c < cols:
                for dr, dc in direction:
                    if 0<=r+dr<rows and 0<=c+dc<cols and (r+dr, c+dc) not in visited and grid[r+dr][c+dc] == "1":
                        dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    count += 1
                    # print(visited)
        return count
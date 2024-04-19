class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1,0), (0,1), (0,-1)]
        for r in range(rows):
            for c in range(cols):
                grid[r][c] = int(grid[r][c])
        def dfs(r,c):
            visited.add((r,c))
            for dr, dc in directions:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and (r+dr, c+dc) not in visited and grid[r+dr][c+dc] == 1:
                    dfs(r+dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    res+=1
                    dfs(r,c)
        
        return res

        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = set()
        def dfs(r,c):
            if (r,c) in visited:
                return
            visited.add((r,c))
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == "0":
                return
            
            for new_r, new_c in [(r-1, c), (r+1, c), (r, c-1), (r,c+1)]:
                if (new_r, new_c) not in visited:
                    dfs(new_r, new_c)
            

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        return count 
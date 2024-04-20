class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        stack = []
        def dfs(r,c):
            if c+1 < cols and grid[r][c+1] == 1:
                return dfs(r, c+1)
            if r+1 < rows and grid[r+1][c] == 1:
                return dfs(r+1, c)
            return [r,c]
        res = []
        visited = set()
        for r in range(rows):
            for c in range(cols):
                valid = True
                if grid[r][c] == 1 and (r,c) not in visited:
                    a,b = dfs(r,c)
                    res.append([r,c,a,b])   
                    for l in range(r, a+1):
                        for k in range(c, b+1):
                            visited.add((l,k))
                    # print(res)
        return res

            

            




        
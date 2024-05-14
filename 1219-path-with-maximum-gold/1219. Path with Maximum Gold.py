class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1,0), (0,-1), (0,1)]
        def dfs(r,c, visited, currSum):
            if (r,c) in visited:
                return currSum
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return currSum
            if grid[r][c] == 0:
                return currSum
            res = 0
            for dr, dc in directions:
                visited.add((r,c))
                res = max(res, dfs(r+dr, c+dc, visited, currSum + grid[r][c]))
                visited.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                possible_sum = dfs(r,c, set(), 0)
                res = max(res, possible_sum)
                print(possible_sum)
        return res

        
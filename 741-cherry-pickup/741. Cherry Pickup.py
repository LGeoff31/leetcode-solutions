class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # We can traverse the grid twice
        # Note that this is essentially equivalent to traverseing to (n-1, n-1) in two differnt paths, trying grab as much possible
        # Don't want to overlap the paths ideally, that way we can maximize cheerry picks
        # Time constraints are very small, O(n^4) would work
        # If we think of the simpler question of just getting to (n-1, n-1) in one path, we can use DP O(n^2)
        # Hence, why don't we just run this algorithm twice??
        # The issue is we want the path we took that way we can update the board
        # However, it may not always be efficient to greddily take the most amount cherries possible in the first go
        # THis is because perhaps you add more seperation between the next path you run
        n = len(grid)
        @cache
        def dfs(r1, c1, r2, c2):
            if not(0<=r1<n and 0<=c1<n and 0<=r2<n and 0<=c2<n):
                return -1e9
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -1e9
            if r1 == n-1 and c1 == n-1 and r2 == n-1 and c2 == n-1:
                return grid[r1][c1]

            ans = grid[r1][c1]
            if r1 != r2:
                ans += grid[r2][c2]
            
            return ans + max(
                dfs(r1+1, c1, r2+1, c2),
                dfs(r1+1, c1, r2, c2+1),
                dfs(r1, c1+1, r2+1, c2),
                dfs(r1, c1+1, r2, c2+1),
            )
        ans = dfs(0, 0, 0, 0)
        return ans if ans > -99999999 else 0
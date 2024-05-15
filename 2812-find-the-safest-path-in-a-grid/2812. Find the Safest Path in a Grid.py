class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        inf = math.inf

        # step 1: calculate distance of each node to closest thieves by 2 pass DP
        dp = [[inf] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i-1][j] if i - 1 >= 0 else inf, 
                                    dp[i][j-1] if j - 1 >= 0 else inf)
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0:
                    dp[i][j] = min(dp[i][j],
                        (1 + dp[i+1][j]) if i + 1 < n else inf, 
                        (1 + dp[i][j+1]) if j + 1 < n else inf)

        # step 2: define reachable with thresholding the safety
        def reachable(minSafety):
            visited = set()
            visited.add((0, 0))

            def dfs(r, c):
                if r == n - 1 and c == n - 1:
                    return True
                DIR = [0, 1, 0, -1, 0]
                for dr, dc in zip(DIR[:4], DIR[1:]):
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < n and 0 <= nc < n
                        and (nr, nc) not in visited
                        and dp[nr][nc] >= minSafety):
                        visited.add((nr, nc))
                        if dfs(nr, nc):
                            return True
                return False
            return dfs(0, 0)
                    
        # step 3: binary search
        lo, hi = 0, min(dp[0][0], dp[n-1][n-1])

        while lo < hi:
            mid = (lo + hi) // 2
            if not reachable(mid):
                hi = mid
            else:
                lo = mid + 1
        if reachable(lo):
            return lo
        return lo-1
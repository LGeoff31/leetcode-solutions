class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if m == 1:
            return 0

        # prefix sum per column
        col = [[0]*(n+1) for _ in range(m)]
        for j in range(m):
            for i in range(n):
                col[j][i+1] = col[j][i] + grid[i][j]

        dp = [[0]*(n+1) for _ in range(n+1)]
        prefMax = [[0]*(n+1) for _ in range(n+1)]
        suffMax = [[0]*(n+1) for _ in range(n+1)]

        for c in range(1, m):

            newdp = [[0]*(n+1) for _ in range(n+1)]

            for curr in range(n+1):
                for prev in range(n+1):

                    if curr <= prev:
                        gain = col[c][prev] - col[c][curr]

                        newdp[curr][prev] = max(
                            newdp[curr][prev],
                            suffMax[prev][0] + gain
                        )
                    else:
                        gain = col[c-1][curr] - col[c-1][prev]

                        newdp[curr][prev] = max(
                            newdp[curr][prev],
                            suffMax[prev][curr],
                            prefMax[prev][curr] + gain
                        )

            # build prefix & suffix
            for curr in range(n+1):

                prefMax[curr][0] = newdp[curr][0]

                for prev in range(1, n+1):
                    penalty = 0
                    if prev > curr:
                        penalty = col[c][prev] - col[c][curr]

                    prefMax[curr][prev] = max(
                        prefMax[curr][prev-1],
                        newdp[curr][prev] - penalty
                    )

                suffMax[curr][n] = newdp[curr][n]

                for prev in range(n-1, -1, -1):
                    suffMax[curr][prev] = max(
                        suffMax[curr][prev+1],
                        newdp[curr][prev]
                    )

            dp = newdp

        ans = 0
        for k in range(n+1):
            ans = max(ans, dp[0][k], dp[n][k])

        return ans
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        non_exist = {1,2,3} - set(colors)
        # dp[i][x] = closest distance to x starting at i
        dp = [[1e9, 1e9, 1e9] for _ in range(len(colors))]
        # FORWARD
        dp[0][0] = 0 if colors[0] == 1 else 1e9
        dp[0][1] = 0 if colors[0] == 2 else 1e9
        dp[0][2] = 0 if colors[0] == 3 else 1e9
        for i in range(1, len(colors)):
            dp[i][0] = 0 if colors[i] == 1 else 1e9
            dp[i][1] = 0 if colors[i] == 2 else 1e9
            dp[i][2] = 0 if colors[i] == 3 else 1e9
            for j in range(3):
                dp[i][j] = min(dp[i][j], 1 + dp[i-1][j])
        print(dp)
        # BACKWARD
        # dp[-1][0] = 0 if colors[-1] == 1 else 1e9
        # dp[-1][1] = 0 if colors[-1] == 2 else 1e9
        # dp[-1][2] = 0 if colors[-1] == 3 else 1e9
        for i in range(len(colors) -2, -1, -1):
            # dp[i][0] = 0 if colors[i] == 1 else 1e9
            # dp[i][1] = 0 if colors[i] == 2 else 1e9
            # dp[i][2] = 0 if colors[i] == 3 else 1e9
            for j in range(3):
                dp[i][j] = min(dp[i][j], 1 + dp[i+1][j])
        a = []
        for u,v in queries:
            if v in non_exist:
                a.append(-1)
            else:
                a.append(dp[u][v-1])
        return a
        # return list(dp[u][v-1] for u,v in queries)

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Attempt on Floyd Warshall's algorithm -> gives you the shortest distance between any two points on a weighted graph in O(N^3)

        dp = [[1e9] * n for _ in range(n)]
        # Fill diagonal with 0
        for i in range(n):
            dp[i][i] = 0
        
        for u, v, w in edges: # Kinda makes a relective dp square
            dp[u][v] = w
            dp[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k] < 1e9 and dp[k][j] < 1e9:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        res = -1
        minCount = 1e9
        for r in range(n):
            count = 0
            for c in range(n):
                if r != c and dp[r][c] <= distanceThreshold:
                    count += 1
            minCount = min(minCount, count)

        for r in range(n):
            count = 0
            for c in range(n):
                if r!=c and dp[r][c] <= distanceThreshold:
                    count += 1
            if count == minCount:
                res = max(res, r)
        return res
            
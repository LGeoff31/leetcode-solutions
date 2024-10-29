class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # dp[i][j] = accumulated cost of painting house i with color j
        houses = len(costs)
        colors = len(costs[0])
        dp = [[1e9] * colors for _ in range(houses)]
        
        # Fill in the ways of painting house 1
        for c in range(colors):
            dp[0][c] = costs[0][c]
        for h in range(1, houses):
            for c in range(colors):
                for dc in range(colors):
                    if c != dc:
                        dp[h][c] = min(dp[h][c], dp[h-1][dc] + costs[h][c])
        print(dp)
        return min(dp[-1])
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [1e9] * (len(cost))
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost)):
            dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])
        return min(cost[-2] + dp[-2], dp[-1] + cost[-1])
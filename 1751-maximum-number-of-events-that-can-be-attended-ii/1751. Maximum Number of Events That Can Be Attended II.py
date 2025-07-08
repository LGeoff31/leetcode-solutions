class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        dp[i][k] = max value you can achieve ending on index i after taking k events
        dp[i][k] = dp[i-1][k] if overlap with prevIdx else max(dp[i-1][k], dp[i-1][k-1] + events[i-1][2])
        """
        events.sort()
        start_indicies = [s for s, _, _ in events]
        stack = []
        @cache
        def dfs(i, taken): #O(n * sum(values) * k)
            if taken > k:
                return -1e9
            if i == len(events):
                return 0
            return max(events[i][2] + dfs(bisect_right(start_indicies, events[i][1]), taken + 1), dfs(i+1, taken))
        return dfs(0, 0)
            
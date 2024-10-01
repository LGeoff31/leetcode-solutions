class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dfs(i):
            if i == len(days):
                return 0
            res = 1e9
            # Try 1 day
            res = min(res, costs[0] + dfs(i + 1))
            
            # Try 7 days
            next_idx = bisect.bisect_left(days, days[i] + 7)
            res = min(res, costs[1] + dfs(next_idx))

            # Try 30 days
            next_idx = bisect.bisect_left(days, days[i] + 30)
            res = min(res, costs[2] + dfs(next_idx))

            return res
        
        return dfs(0)
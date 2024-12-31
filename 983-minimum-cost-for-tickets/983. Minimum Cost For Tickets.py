class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dfs(idx):
            if idx == len(days):
                return 0
            # res = 1e9
            # # Try 1 day
            # res = min(res,  dfs(bisect_right(days, days[idx] + 1)))
            # # Try 7 days
            # res = min(res, dfs(bisect_right(days, days[idx] + 7)))
            # # Try 30 days
            # res = min(res, dfs(bisect_right(days, days[idx] + 30)))
            return min(costs[0] + dfs(bisect_right(days, days[idx] + 1 - 1)), costs[1] + dfs(bisect_right(days, days[idx] + 7 - 1)), costs[2] + dfs(bisect_right(days, days[idx] + 30 - 1)))

        return dfs(0)
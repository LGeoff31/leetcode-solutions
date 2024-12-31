class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dfs(idx):
            if idx == len(days):
                return 0
            return min(costs[0] + dfs(bisect_left(days, days[idx] + 1)), costs[1] + dfs(bisect_left(days, days[idx] + 7)), costs[2] + dfs(bisect_left(days, days[idx] + 30)))

        return dfs(0)
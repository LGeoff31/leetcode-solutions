class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        start_times = [s for s, _, _ in events]
        print(events)
        print(start_times)
        @cache
        def dfs(idx, taken):
            if idx == len(events):
                return 0 if taken <= 2 else -1e9
            
            if taken > 2:
                return -1e9
            
            res = 0
            # TAKE
            end = events[idx][1]
            value = events[idx][2]
            nxt_available_idx = bisect_right(start_times, end)
            print('geo', nxt_available_idx)
            res = max(res, value + dfs(nxt_available_idx, taken+1))
            # DONT TAKE
            res = max(res, dfs(idx + 1, taken))
            return res
        return dfs(0, 0)
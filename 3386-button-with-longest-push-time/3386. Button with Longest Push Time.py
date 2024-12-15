class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        indexes = [a for a,b in events]
        times = [events[0][1]]
        for i in range(1, len(events)):
            times.append(events[i][1] - events[i-1][1])
        print(times)
        res = []
        target = max(times)
        for i, time in enumerate(times):
            if time == target:
                res.append(i)
        print(res)
        ans = 1e9
        for i, (a,b) in enumerate(events):
            if i in res:
                ans = min(ans, events[i][0])
        return ans
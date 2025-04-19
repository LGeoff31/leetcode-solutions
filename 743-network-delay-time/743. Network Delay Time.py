class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0

        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        h = []
        heapq.heappush(h, (0, k))

        times = [1e9] * n
        times[k-1] = 0
        while len(h) > 0:
            t, node = heapq.heappop(h)

            if t > times[node-1]: continue
            for new_pos, new_time in graph[node]:
                if t + new_time < times[new_pos-1]:
                    times[new_pos-1] = t + new_time
                    heapq.heappush(h, (t+new_time, new_pos))
        print(times)
        return max(times) if max(times) != 1e9 else -1
        
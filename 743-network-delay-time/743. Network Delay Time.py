class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dic = defaultdict(list)
        for u,v,w in times:
            dic[u].append((w, v))
        minHeap = [(0, k)]
        res = {k: 0}
        print(dic)
        while minHeap:
            weight, node = heappop(minHeap)

            for w, v in dic[node]:
                if v in res and res[v] <= w+weight:
                    continue
                res[v] = w+weight
                heappush(minHeap, (w+weight, v))
        return max(res.values()) if len(res) == n else -1

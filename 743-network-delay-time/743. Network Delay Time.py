class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = [(0, k)]
        res = {k:0} # {2: 0}
        adj = defaultdict(list) # node : [(nei, weight), ...]
        for u,v, w in times:
            adj[u].append((v, w))
        # print(adj)
        while minHeap:
            weight, node = heappop(minHeap)
            print('weight', weight, 'node', node)
            # res[node] = weight
            for nei, w in adj[node]:
                if nei not in res:
                    heappush(minHeap, (w+weight, nei))
                    res[nei] = w+weight
                else:
                    if w+weight < res[nei]:
                        res[nei] = w+weight
                        heappush(minHeap, (w+weight, nei))
        print(res)
        if len(res) != n:
            return -1
        return max(res.values())


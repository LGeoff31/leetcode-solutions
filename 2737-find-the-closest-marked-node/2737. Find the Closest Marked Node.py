class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        # n nodes that are connected by weighted edges
        # starting node s, find min distance to get to marked node
        # -1 if there is no path to get one
        marked = set(marked)
        minHeap = [(0, s)]
        adj = defaultdict(list)
        res = {s: 0}
        for u,v,w in edges:
            adj[u].append((v, w))
        # res = 1e9
        while minHeap:
            weight, node = heappop(minHeap)

            for nei, w in adj[node]:
                if nei not in res:
                    res[nei] = w+weight
                    heappush(minHeap, (w+weight, nei))
                else:
                    if w+weight < res[nei]:
                        res[nei] = w+weight
                        heappush(minHeap, (w+weight, nei))
        ans = 1e9
        for key in res:
            if key in marked:
                ans = min(ans, res[key])
        print(res)
        return ans if ans != 1e9 else -1

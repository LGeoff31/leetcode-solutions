class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        adj = defaultdict(list)
        for u,v,w in roads:
            adj[u].append((w, v))
            adj[v].append((w, u))
        minHeap = [(0, 0)]
        count = [0] * n
        count[0] = 1
        res = {0 : 0}

        while minHeap:
            weight, node = heappop(minHeap)

            for w, nei in adj[node]:
                if nei not in res or weight+w < res[nei]:
                    res[nei] = weight + w
                    heappush(minHeap, (w+weight, nei))
                    count[nei] = count[node]
                elif weight+w == res[nei]:
                    count[nei] += count[node] % MOD
                    # heappush(minHeap, (weight+w, nei))
        print(count)
        return count[n-1] % MOD
                
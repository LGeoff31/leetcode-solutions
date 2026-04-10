class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        dist = {i+1 : 1e9 for i in range(n)}
        dist[k] = 0
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v, t))

        queue = deque([(k, 0)]) 
        while queue:
            node, weight = queue.popleft()

            for nei, nei_weight in adj[node]:
                if weight + nei_weight < dist[nei]:
                    dist[nei] = weight + nei_weight
                    queue.append((nei, weight+nei_weight))
        res = max(dist.values()) if max(dist.values()) != 1e9 else -1
        return res


            
class Solution:
    def __init__(self):
        self.graph = []
    
    def dijkstra(self, n):
        dist = [1e9] * n
        dist[0] = 0
        pq = [(0, 0)] #distance, node
        while pq:
            cd, node = heapq.heappop(pq)
            if node == n-1:
                return dist[n-1]
            if cd > dist[node]:
                continue
            for nei, wt in self.graph[node]:
                if wt + cd < dist[nei]:
                    dist[nei] = wt+cd
                    heapq.heappush(pq, (wt+cd, nei))
        return dist[-1]
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        self.graph = [[] for _ in range(n)]
        for i in range(n-1):
            self.graph[i].append((i+1, 1))
        res = []
        for u,v in queries:
            self.graph[u].append((v,1))
            res.append(self.dijkstra(n))
        return res
        
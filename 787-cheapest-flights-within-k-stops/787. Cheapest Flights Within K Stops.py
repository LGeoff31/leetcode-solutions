class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v, weight in flights:
            adj[u].append((v, weight))
        
        res = float('inf')
        queue = deque([(src, 0)])
        distances = {src : 0}
        while queue:
            for i in range(len(queue)):
                node, weight = queue.popleft()
                if node == dst:
                    res = min(res, distances[node])
                    continue
                
                if k == -1:
                    continue

                for nei, nei_weight in adj[node]:
                    if nei not in distances or weight+nei_weight < distances[nei]:
                        distances[nei] = weight + nei_weight
                        queue.append((nei, weight + nei_weight))
            k -= 1
        

        return res if res != float('inf') else -1

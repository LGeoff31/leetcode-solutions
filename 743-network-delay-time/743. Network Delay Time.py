class Solution:
    def networkDelayTime(self, edges: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            
        minHeap = [(0, k)] # (weight, node)
        dist = {k: 0}
            
        while minHeap:
            weight, node = heappop(minHeap)
            for nei, nei_weight in adj[node]:
                print(nei)
                if nei in dist and dist[nei] <= weight + nei_weight:
                    continue 
                dist[nei] = weight + nei_weight 
                heappush(minHeap, (weight + nei_weight, nei))
        print(dist)
        return max(dist.values()) if len(dist) == n else -1
        

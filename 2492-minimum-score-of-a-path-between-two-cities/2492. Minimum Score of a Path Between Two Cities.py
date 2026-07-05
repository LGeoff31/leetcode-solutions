class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        queue = deque([1])
        res = float('inf')
        adj = defaultdict(list)
        seen = set()
        seen_nodes = {1}
        for u, v, distance in roads:
            adj[u].append((v, distance))
            adj[v].append((u, distance))


        while queue:
            node = queue.popleft()
            for nei, dis in adj[node]:
                if (node, nei) not in seen:
                    seen.add((node, nei))
                    res = min(res, dis)
                    if nei not in seen_nodes:
                        seen_nodes.add(nei)
                        queue.append(nei)
        return res

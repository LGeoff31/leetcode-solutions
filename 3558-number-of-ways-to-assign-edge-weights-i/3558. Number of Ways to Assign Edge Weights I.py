class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        seen = {1}
        queue = deque([1])
        steps = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                for nei in adj[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
            steps += 1
        
        return 2 ** (steps-2) % MOD


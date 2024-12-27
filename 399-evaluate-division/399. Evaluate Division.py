class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, (u,v) in enumerate(equations):
            adj[u].append((v, values[i]))
            adj[v].append((u, 1/values[i]))
        
        def bfs(start, end):
            if start == end and start in adj: return 1
            # -1 if start or end do no exist in graph

            queue = deque([(start, 1)])
            visited = set()
            visited.add(start)
            while queue:
                for i in range(len(queue)):
                    node, weight = queue.popleft()
                    if node not in adj: return -1
                    if node == end:
                        return weight
                    for n, w in adj[node]:
                        if n not in visited:
                            visited.add(n)
                            queue.append((n, w * weight))
            return -1

        res = []
        for start, end in queries:
            res.append(bfs(start, end))
        return res
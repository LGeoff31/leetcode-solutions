class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) #maps a -> list of [b, a/b]
        for i, eq in enumerate(equations):
            a,b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q, visited = deque(), set()
            q.append([src, 1])
            visited.add(src )
            while q:
                for i in range(len(q)):
                    currElem, val = q.popleft()
                    if currElem == target: return val
                    for n, w in adj[currElem]:
                        if n not in visited:
                            q.append([n, val * w])
                            visited.add(n)

            return -1

        
        res = []

        for q in queries:
            result = bfs(q[0], q[1])
            res.append(result)
        return res


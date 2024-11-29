class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        # kahns for cycle
        # multi source bfs for distances
        graph = defaultdict(list)
        deg = [0 for i in range(n)]
        ret = [0 for i in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            deg[a] += 1
            deg[b] += 1

        queue = deque()
        visited = [False for i in range(n+1)]
        for i in range(n):
            if deg[i] == 1:
                queue.append(i)

        while queue:
            node = queue.popleft()
            deg[node] -= 1
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    # have not visited yet
                    deg[nei] -= 1
                    if deg[nei] == 1:
                        queue.append(nei)

        visited = [False for i in range(n+1)]
        queue = deque()
        for i in range(n):
            if deg[i] != 0:
                queue.append((i, 0))
                visited[i] = True

        while queue:
            node, dist = queue.popleft()
            ret[node] = dist
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    queue.append((nei, dist + 1))
        
        return ret
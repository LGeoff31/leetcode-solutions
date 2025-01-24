class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
     
        queue = deque([])
        adj = defaultdict(list)
        for i in range(n):
            arr = graph[i]
            for elem in arr:
                adj[elem].append(i)
                indegree[i] += 1
        res = [False] * n

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                res[i] = True
                
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                res[node] = True
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
                
        ans = [i for i in range(len(res)) if res[i]]
        return ans
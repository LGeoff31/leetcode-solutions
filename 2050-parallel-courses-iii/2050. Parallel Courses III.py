class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        indegree = [0] * n
        graph = defaultdict(list) # directed graph preq -> real course

        for u,v in relations:
            graph[u - 1].append(v - 1)
            indegree[v - 1] += 1
        
        queue = deque([])
        dist = defaultdict(int)
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dist[i] = time[i]
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                indegree[nei] -= 1
                dist[nei] = max(dist[nei], time[nei] + dist[node])

                if indegree[nei] == 0:
                    queue.append(nei)
        return max(dist.values())
        
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        indegree = [0] * n
        min_dist = defaultdict(int)
        for u,v in relations:
            adj[u-1].append(v-1)
            indegree[v-1] += 1
        
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                min_dist[i] = time[i]

        while queue:
            node = queue.popleft()
            for nei in adj[node]:
                indegree[nei] -= 1
                min_dist[nei] = max(min_dist[nei], min_dist[node] + time[nei])
                if indegree[nei] == 0:
                    queue.append(nei)
        return max(min_dist.values())

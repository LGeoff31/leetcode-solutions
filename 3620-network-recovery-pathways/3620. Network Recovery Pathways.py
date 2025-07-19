class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = defaultdict(list)
        indegree = [0] * n
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                indegree[v] += 1

        t = []
        queue = deque([i for i in range(n) if indegree[i] == 0 and online[i]]) 
        while queue:
            u = queue.popleft()
            t.append(u)
            for v, _ in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        def valid(threshold):
            dist = [inf] * n # dist[i] distance from node 0 to node i
            dist[0] = 0
            for node in t:
                if dist[node] == inf:
                    # This mean not all desendents have been reached
                    continue
                for v, cost in adj[node]:
                    if cost < threshold:
                        continue
                    if dist[node] + cost < dist[v]:
                        dist[v] = dist[node] + cost

            return dist[-1] <= k
        costs = sorted([c for _, _, c in edges])
        l, r = 0, len(costs) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if valid(costs[mid]):
                # You can find a path where all edges are above mid
                res = costs[mid]
                l = mid + 1
            else:
                r = mid - 1
        return res
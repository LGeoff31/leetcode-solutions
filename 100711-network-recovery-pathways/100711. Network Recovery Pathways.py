class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        """
        Remove all offline nodes and links to offline nodes
        DAG -> topologial sort
        """
        n = len(online)
        adj = defaultdict(list)
        indegree = [0] * n
        for u,v, cost in edges:
            # DONT ADD OFFLINE EDGE
            if not(online[u] == False or online[v] == False):
                adj[u].append((v,cost))
                indegree[v] += 1
        # print(adj)
        t = [] # This gives us the order in which to traverse the DAG
        q = deque([i for i in range(n) if (indegree[i] == 0)]) # starting points
        while q:
            node = q.popleft()
            t.append(node) 
            for v, _ in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        # dp = [None] * n # dp[node] = (totalCost, minEdge) for the best path to node
        # dp[0] = (0, 1e9)
        # for i in range(n):
        #     if indegree[i] == 0:
        #         dp[i] = (0, 1e9)
        # print(t)
        # for node in t:
        #     if dp[node] is None:
                # Not visitied yet
                # dp[node] = (9, 1e9)
            #     continue
            # currCost, currMinEdge = dp[node]
            # for v, cost in adj[node]:
            #     nxtCost = currCost + cost
            #     if nxtCost > k:
            #         # Can't go
            #         continue
            #     nxtMinEdge = min(currMinEdge, cost)
            #     if dp[v] is None or nxtMinEdge > dp[v][1] or (nxtMinEdge == dp[v][1] and nxtCost < dp[v][0]):
            #         dp[v] = (nxtCost, nxtMinEdge)
        costs = sorted(c for _, _, c in edges)
        def valid(threshold):
            dist = [inf] * n # distance to node i
            dist[0] = 0
            for u in t:
                if dist[u] == inf:
                    continue
                for v,c in adj[u]:
                    if c < threshold:
                        continue
                    new_cost = dist[u] + c
                    if new_cost < dist[v]:
                        dist[v] = new_cost
            return dist[n-1]<= k
        l, r = 0, len(costs) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if valid(costs[mid]):
                res = costs[mid]
                l = mid + 1
            else:
                r = mid - 1
        return res
        # print(dp)
        # return dp[n-1][1] if dp[n-1] else -1
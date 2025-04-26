class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        # 1. What is the minimum distance path
        # 2. Find all paths from 0 -> n-1 with that distance

        # Idea: For every node, find the minimum distance to get to that node from node 0
        # If you reach a node with a current weight > that amount, it is definitely not apart of the path
        # So each time you reach a node with weight = to that path, dp[node] += 1
        # We want to return dp[n-1]


        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        res = {0: 0}
        minHeap = [(0,0)]

        while minHeap:
            wei, node = heappop(minHeap)
            if res[node] < wei: continue
            for nei, nei_wei in adj[node]:
                if nei in res and wei+nei_wei >= res[nei]:
                    continue
                res[nei] = wei + nei_wei
                heappush(minHeap, (wei + nei_wei, nei))
        # O(V + VLOGE)
        if n-1 not in res:
            return [False] * len(edges)
        total_distance = res[n-1]
        queue = deque([[n-1, 0]])
        valid_edges = {}
        visited = set([n-1])
        while queue:
            for i in range(len(queue)):
                node, curr_weight = queue.popleft()
                for nei, nei_weight in adj[node]:
                    if curr_weight+nei_weight+res[nei] == total_distance:
                        if (node, nei) not in valid_edges and (nei, node) not in valid_edges:
                            if nei not in visited:
                                visited.add(nei)
                                queue.append((nei, curr_weight + nei_weight))
                        valid_edges[(node, nei)] = True

        res = [False] * len(edges)
        for i in range(len(edges)):
            u,v,_ = edges[i]
            if (u,v) in valid_edges or (v,u) in valid_edges:
                res[i] = True

        return res
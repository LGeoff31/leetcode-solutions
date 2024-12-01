from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2, k):
        if k == 0:
            return [1] * (len(edges1) + 1)
        def bfs(adj, start, max_depth):
            dist = [0] * (max_depth + 1)
            queue = deque([start])
            visited = set([start])
            depth = 0
            
            while queue and depth <= max_depth:
                size = len(queue)
                dist[depth] = size if depth == 0 else dist[depth - 1] + size
                for _ in range(size):
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                depth += 1
            
            for i in range(depth, max_depth + 1):
                dist[i] = dist[i - 1]
            return dist
        
        # Build adjacency lists
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)
        
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        
        # Precompute BFS results for both trees
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        bfs1 = [bfs(adj1, i, k) for i in range(n)]
        bfs2 = [bfs(adj2, i, k) for i in range(m)]
        
        # Compute results for each node in the first tree
        result = []
        for i in range(n):
            max_nodes = 0
            for j in range(m):
                max_nodes = max(max_nodes, bfs1[i][k] + bfs2[j][k - 1])
            result.append(max_nodes)
        
        return result

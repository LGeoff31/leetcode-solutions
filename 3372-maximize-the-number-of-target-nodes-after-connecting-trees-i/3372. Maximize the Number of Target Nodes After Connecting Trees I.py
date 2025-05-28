class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)

        for u,v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u,v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        n, m = len(edges1) + 1, len(edges2) + 1  
        if k == 0: return [1] * n
        def bfs(node, adj, expansions):
            queue = deque([node])
            count = 1
            visited = set()
            visited.add(node)
            while queue and expansions > 0:
                for i in range(len(queue)):
                    node = queue.popleft()
                    for nei_node in adj[node]:
                        if nei_node not in visited:
                            visited.add(nei_node)
                            queue.append(nei_node)
                            count += 1
                expansions -= 1
                # print(queue, visited, expansions)
            return count
        precompute1 = {}
        precompute2 = {}
        for i in range(n):
            precompute1[i] = bfs(i, adj1, k)
        for i in range(m):
            precompute2[i] = bfs(i, adj2, k-1) # You go k-1 edges times
        print(precompute1)
        print(precompute2)

        res = [0] * n
        max_reach=max(precompute2.values())
        for i in range(n):
            res[i] = max(res[i], precompute1[i] + max_reach)
        return res



class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        adj1, adj2 = defaultdict(list), defaultdict(list)
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u,v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        dic1 = {}
        dic2 = {}

        n, m = len(edges1) + 1, len(edges2) + 1
        
        # bfs on the second tree to populate dic1
        def bfs(adj):
            queue = deque([0])
            odd, even = 0, 1
            visited = set()
            visited.add(0)
            looking_even = False
            while queue:
                for i in range(len(queue)):
                    node = queue.popleft()
                    for nei in adj[node]:
                        if nei in visited:
                            continue
                        visited.add(nei)
                        queue.append(nei)
                        if looking_even:
                            even += 1
                        else:
                            odd += 1
                
                looking_even = not looking_even
            return odd,even

        odd1, even1 = bfs(adj1)
        odd2, even2 = bfs(adj2)

        odd_nodes, even_nodes = set(), set()
        q = deque([0])
        even = True
        v = set()
        v.add(0)
        while q:
            for i in range(len(q)):
                z = q.popleft()
                if not even:
                    odd_nodes.add(z)
                else:
                    even_nodes.add(z)
                for nei in adj1[z]:
                    if nei in v:
                        continue
                    v.add(nei)
                    q.append(nei)
            even = not even
        print(even_nodes)
        print(odd_nodes)
        print()
        print(even1, odd1)
        print(even2, odd2)
        print()
        res = [0] * n
        print('res', res)
        for i in range(n):
            if i in even_nodes:
                res[i] = even1 + max(odd2, even2)
            else:
                res[i] = odd1 + max(odd2, even2)

        return res


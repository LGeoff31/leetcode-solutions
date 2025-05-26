class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
           adj[u].append(v)
           adj[v].append(u)

        visited = set()
        visited.add(1)

        def maxHeight(node):
            if len(adj[node]) == 1 and adj[node][0] in visited:
                return 1
            h = 0
            for child_node in adj[node]:
                if child_node in visited:
                    continue
                visited.add(child_node)
                h = max(h, 1 + maxHeight(child_node))
            return h

        h = maxHeight(1) 
        print('reached', h)
        MOD = 10 ** 9 + 7
        res = 0
        # for number_ones in range(1, h+1, 2):
        #     res = (res+comb(h, number_ones)) % MOD

        return 2**(h-2) % MOD
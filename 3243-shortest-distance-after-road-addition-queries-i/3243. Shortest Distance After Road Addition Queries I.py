class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Connect a path with adjacent numbers
        adj = defaultdict(list)
        for i in range(n-1):
            adj[i].append(i+1)
        
        def dfs(node, cache):
            if node == n-1:
                return 0
            if node in cache:
                return cache[node]
            res = 1e9
            # print(adj)
            for nei in adj[node]:
                res = min(res, 1 + dfs(nei, cache))
            cache[node] = res
            return res

        res = []
        for u,v in queries:
            adj[u].append(v)
            res.append(dfs(0, {}))
        return res 

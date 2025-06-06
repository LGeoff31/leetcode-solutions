class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in roads:
            adj[u].append(v)
            adj[v].append(u)
        def calc(i, j):
            return len(adj[i]) + len(adj[j]) - (1 if j in adj[i] else 0)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, calc(i, j))
        return res
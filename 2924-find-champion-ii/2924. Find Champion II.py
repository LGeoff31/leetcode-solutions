class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        mostRoot = set()

        adj = defaultdict(list)
        for u, v in edges:
            adj[v].append(u)

        def val(a):
            for key in a:
                return key
        # Dfs(node) -> most parent node
        @cache
        def dfs(node):
            if not adj[node]:
                return node
            visited = set()
            for nei in adj[node]:
                visited.add(dfs(nei))
            if len(visited) > 1: 
                return -1 
            else:
                return val(visited)
        visited = set() 
        for i in range(n):
            visited.add(dfs(i))
        if len(visited) > 1:
            return -1
        return val(visited)
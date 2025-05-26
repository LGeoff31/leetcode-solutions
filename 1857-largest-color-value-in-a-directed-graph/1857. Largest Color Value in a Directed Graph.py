class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        #O(n^2)
        n = len(colors)
        adj = {}
        for i in range(n):
            adj[i] = []
        for u,v in edges:
            adj[u].append(v)
        # @cache
        def dfs(node):
            if node in path:
                return 1e9
            if node in visited:
                return 0
            visited.add(node)
            path.add(node)
            colorIndex = ord(colors[node]) - ord("a")
            count[node][ord(colors[node]) - ord("a")] = 1
            for nei in adj[node]:
                if dfs(nei) == 1e9:
                    return 1e9
                for c in range(26):
                    count[node][c] = max(count[node][c], (1 if c == colorIndex else 0) + count[nei][c])
            path.remove(node)
            return max(count[node])
        res = 0
        visited = set()
        path = set()
        count = [[0] * 26 for _ in range(n)] #count[node][color] = max freq of that color starting that node
        for i in range(n):
            res = max(res, dfs(i))
            
        return res if res != 1e9 else -1
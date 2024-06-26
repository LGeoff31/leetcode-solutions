class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = []
        graph = defaultdict(list)
        for u, v in edges: #O(E)
            graph[v].append(u)
        @cache
        def dfs(node): #O(V)
            if not graph[node]:
                return []
            ans = []
            for child in graph[node]:
                ans += [child] + dfs(child)
            return list(set(ans))

        for i in range(n): #O(V)
            res.append(sorted(dfs(i)))#O(VlogV)
        return res
        
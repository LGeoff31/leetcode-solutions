class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        infected = set()
        adj = defaultdict(list)
        for u,v in invocations:
            adj[u].append(v)

        def dfs(node):
            if node not in infected:
                infected.add(node)
                for nei in adj[node]:
                    dfs(nei)
        
        dfs(k)

        isAll = False
        
        for node in range(n):
            if not node in infected:
                for nei in adj[node]:
                    if nei in infected:
                        isAll = True
                        break
            if isAll:
                break
        if isAll:
            return list(range(n))
        return [i for i in range(n) if i not in infected]


        return []
                
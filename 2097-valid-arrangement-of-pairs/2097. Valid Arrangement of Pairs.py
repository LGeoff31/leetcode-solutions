class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Each pair represents a node
        # An edge connects between two valid pairs
        
        adj = defaultdict(list)
        degree = defaultdict(int)

        for u,v in pairs:
            adj[u].append(v)
            degree[u] += 1
            degree[v] -= 1
        start = u
        for key in degree:
            if degree[key] == 1:
                start = key
                break 
        ans = []
        def dfs(node):
            while adj[node]:
                dfs(adj[node].pop())
            ans.append(node)
        dfs(start)
        ans.reverse()
        print(ans)
        return [[ans[i], ans[i+1]] for i in range(len(ans) - 1)]

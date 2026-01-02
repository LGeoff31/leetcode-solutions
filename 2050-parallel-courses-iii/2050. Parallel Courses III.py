class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n
        adj = defaultdict(list)
        for u,v in relations:
            indegree[v-1] += 1
            adj[u].append(v)
        @cache
        def dfs(node):
            if len(adj[node]) == 0:
                return time[node - 1]
            res = 0
            for nei in adj[node]:
                res = max(res, time[node - 1] + dfs(nei))
            return res
        res = 0
        starting_nodes = [i+1 for i in range(len(indegree)) if indegree[i] == 0]
        for starting_node in starting_nodes:
            res = max(res, dfs(starting_node))
        return res
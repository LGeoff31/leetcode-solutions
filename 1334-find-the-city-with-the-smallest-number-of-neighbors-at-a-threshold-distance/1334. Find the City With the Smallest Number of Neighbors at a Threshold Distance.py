class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # For each node, dfs to its neighbors to see if distance still less than threshhold, add to set if it is, if you come across something already in the set, update distance to be minimum
        # Store in res array, at the end filter by length then by value

        res = [[] for _ in range(n)]

        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append([v,w])
            adj[v].append([u, w])
        
        def dfs(i, node, distance, dic):
            if distance > distanceThreshold:
                return
            if i != node: res[i].append(node)
            if node in dic and dic[node] <= distance:
                return
            dic[node] = distance
            
            for nei, weight in adj[node]:
                dfs(i, nei, distance + weight, dic)
        
        for i in range(n):
            dfs(i, i, 0, {})
        # print(res)
        ans = []
        for arr in res:
            ans.append(list(set(arr)))
        minLen = 1e9
        for i in ans:
            minLen = min(minLen, len(i))
        res = -1
        print(minLen)
        for i in range(len(ans)):
            if len(ans[i]) == minLen:
                res = i
                print(res)
        print(ans)
        return res


        
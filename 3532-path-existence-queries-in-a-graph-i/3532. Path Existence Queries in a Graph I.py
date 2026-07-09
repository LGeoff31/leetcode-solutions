class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        adj = {}
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i-1]) <= maxDiff:
                adj[i-1] = i
        groups = []
        seen = set()

        def bfs(node, id):
            res = []
            queue = deque([node])
            while queue:
                node = queue.popleft()
                seen.add(node)
                res.append(node)
                if node not in adj:
                    break
                queue.append(adj[node])
            for node in res:
                dic[node] = id
            groups.append(set(res))
        dic = {}
        for i in range(n):
            if i not in seen:
                bfs(i, i)
        res = []
        for a,b in queries:
            if dic[a] == dic[b]:
                res.append(True)
            else:
                res.append(False)
        return res
            
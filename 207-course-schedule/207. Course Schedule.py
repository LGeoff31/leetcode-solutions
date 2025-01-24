class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        indegree = [0] * numCourses  
        adj = defaultdict(list)
        for u, v in prerequisites:
            indegree[u] += 1
            adj[v].append(u)
        queue = deque([])


        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        res = [False] * numCourses
        while queue:
            node = queue.popleft()
            res[node] = True

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    res[nei] = True
                    queue.append(nei)
        check_all_true = lambda res : all(res)
        return all(res)

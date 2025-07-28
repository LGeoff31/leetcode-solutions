class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        indegree = [0] * numCourses
        dic = defaultdict(list)
        for u, v in prerequisites:
            indegree[u] += 1
            dic[v].append(u)
        
        visited = set()
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        # print(queue)
        while queue:
            node = queue.popleft()
            if indegree[node] == 0:
                visited.add(node)
                for nei in dic[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
        return len(visited) == numCourses

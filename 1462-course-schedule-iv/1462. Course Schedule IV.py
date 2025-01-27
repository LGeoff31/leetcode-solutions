class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        res = [False] * len(queries)
        dic = defaultdict(set) # course : [list of preq]
        def valid(start, visited): 
            queue = deque([start])
            seen = set()
            seen.add(start)
            while queue:
                for i in range(len(queue)):
                    node = queue.popleft()
                    for nei in adj[node]:
                        if nei not in seen:
                            queue.append(nei)
                            seen.add(nei)
                            visited.add(nei)    
        print('rea')
        for i in range(numCourses):
            valid(i, dic[i])
        print('reached')
        for i, (start, end) in enumerate(queries): # O(10 ** 4)
            if start in dic[end]:
                res[i] = True
            # res[i] = valid(start, end) # O (100)
        return res
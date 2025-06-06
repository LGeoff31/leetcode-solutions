class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = defaultdict(list)
        for u,v in prerequisites:
            preq[u].append(v)

        self.res = []
        visited = set()
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for p in preq[course]:
                if not dfs(p):
                    return False

            visited.add(course)
            cycle.remove(course)
            self.res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return self.res



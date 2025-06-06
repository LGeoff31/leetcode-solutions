class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        preq = defaultdict(list)
        for u, v in prerequisites:
            preq[u].append(v) # You must take course v to take course u

        cycle = set()
        visited = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)

            visited.add(course)
            
            for p in preq[course]:
                if not dfs(p):
                    return False
            cycle.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        print(visited)
        return numCourses == len(visited)
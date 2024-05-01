class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for u, v in prerequisites:
            graph[u].append(v)
        
        res = []
        visited, cycle = set(), set()

        def dfs(currCourse):
            if currCourse in cycle:
                return False
            if currCourse in visited:
                return True            
            cycle.add(currCourse)
            for preq in graph[currCourse]:
                if not dfs(preq): 
                    return False

            cycle.remove(currCourse)
            visited.add(currCourse)
            res.append(currCourse)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
                


        
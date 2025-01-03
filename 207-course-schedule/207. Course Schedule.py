class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:       
        def dfs(currCourse, visited):
            if currCourse in visited:
                return False
            if len(graph[currCourse]) == 0:
                return True
            
            visited.add(currCourse)
            for preq in graph[currCourse]:
                if dfs(preq, visited) == False: return False 
                graph[currCourse].remove(preq)
            visited.remove(currCourse)
            return True        
        
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
            
        for i in range(numCourses): #run a dfs on each i
            # print(i, graph, dfs(i, set()))
            if not dfs(i, set()): 
                return False
        return True


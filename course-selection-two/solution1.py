class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {c: [] for c in range(numCourses)}
        output = []
        for crs, preq in prerequisites:
            dic[crs].append(preq)

        visited, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for preq in dic[crs]:
                if dfs(preq) == False:
                    return False
            output.append(crs)
            visited.add(crs)
            cycle.remove(crs)

        for i in range(numCourses):
            if dfs(i) == False:
                return []  # there was a cycle

        return output

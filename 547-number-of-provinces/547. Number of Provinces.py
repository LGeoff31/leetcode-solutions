class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        def dfs(idx, arr):
            for i in range(len(arr)):
                if i == idx: continue
                if arr[i] == 1 and i not in visited:
                    visited.add(i)
                    dfs(i, isConnected[i])
                
        islands = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i, isConnected[i])
                islands += 1
        

        return islands
        
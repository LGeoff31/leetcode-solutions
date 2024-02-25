class Solution:
    res = 0
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj=[]
        for i in range(n):
            adj.append([])
        for i in connections:
            adj[i[0]].append([i[1],1])
            adj[i[1]].append([i[0],0])
        def dfs(child,parent):
            for [c, s] in adj[child]:
                if c!=parent:
                    self.res+=s
                    dfs(c,child)
        dfs(0,-1)
        return self.res



        
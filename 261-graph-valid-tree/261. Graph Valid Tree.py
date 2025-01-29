class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, x, y):
        xParent = self.find(x)
        yParent = self.find(y)
        if xParent == yParent: # Already part of same set
            return False 
        if self.rank[xParent] > self.rank[yParent]:
            self.parent[yParent] = xParent
        elif self.rank[xParent] < self.rank[yParent]:
            self.parent[xParent] = yParent
        else:
            self.parent[xParent] = yParent
            self.rank[yParent] += 1
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = UnionFind(n)
        for u,v in edges:
            if dsu.union(u,v) == False:
                return False

        parent = set()
        for i in range(n):
            parent.add(dsu.find(i))
        return len(parent) == 1
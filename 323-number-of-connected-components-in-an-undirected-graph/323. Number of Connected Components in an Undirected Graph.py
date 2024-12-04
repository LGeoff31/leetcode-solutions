class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, a, b):
        aParent = self.find(a)
        bParent = self.find(b)
        if aParent == bParent:
            return False
        if self.parent[aParent] < self.parent[bParent]:
            self.parent[aParent] = bParent
        elif self.parent[aParent] > self.parent[bParent]:
            self.parent[bParent] = aParent
        else:
            self.parent[bParent] = aParent
            self.rank[aParent] += 1        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        for u,v in edges:
            dsu.union(u,v)
        a = set()
        for i in range(n): #bc there are n nodes: 0 to n-1
            a.add(dsu.find(i))
        print(a)
        return len(a)

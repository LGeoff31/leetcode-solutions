class UnionFind():
    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def find(self, x):
        self.parent.setdefault(x, x)
        self.size.setdefault(x, 1)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x,y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x != p_y:
            if self.size[p_x] <= self.size[p_y]:
                p_x, p_y = p_y, p_x
            self.size[p_x] += self.size[p_y]
            self.parent[p_y] = p_x

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind()
        for u,v in edges:
            uf.union(u,v)

        dic = defaultdict(int)
        for i in range(n):
            dic[uf.find(i)] += 1
        res = 0
        print(dic)
        for key in dic:
            res += (dic[key]) * (dic[key]-1) // 2
        return n*(n-1)//2 - res

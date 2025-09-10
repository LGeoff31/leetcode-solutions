class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def find(self, x):
        self.parent.setdefault(x,x)
        self.size.setdefault(x, 1)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x != p_y:
            if self.size[p_x] < self.size[p_y]:
                p_x, p_y = p_y, p_x
            self.size[p_x] += self.size[p_y]
            self.parent[p_y] = p_x

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        for eq in equations:
            if eq[1] == "=":
                uf.union(eq[0], eq[-1])
        for eq in equations:
            if eq[1] == "!":
                if uf.find(eq[0]) == uf.find(eq[-1]):
                    return False
        return True
        
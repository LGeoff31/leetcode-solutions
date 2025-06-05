class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))
        # [1,2,3,4,5 ... 26]
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if y > x:
            self.root[y] = x
        else:
            self.root[x] =y

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        res = ""

        union_structure = UnionFind(26)

        for i in range(len(s1)):
            union_structure.union(ord(s1[i])-97, ord(s2[i])-97)
        
        for c in baseStr:
            res += chr(union_structure.find(ord(c) - 97) + 97)

        return res
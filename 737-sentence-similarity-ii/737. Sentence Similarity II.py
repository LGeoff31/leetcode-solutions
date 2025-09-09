class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        self.parent.setdefault(x,x)
        self.size.setdefault(x,1)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            if self.size[parent_x] < self.size[parent_y]:
                parent_x, parent_y = parent_y, parent_x
            self.size[parent_x] += self.size[parent_y]
            self.parent[parent_y] = parent_x

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        union_find = UnionFind()

        if len(sentence1) != len(sentence2):
            return False

        for a,b in similarPairs:
            union_find.union(a,a)
            union_find.union(b,b)

            union_find.union(a,b)
        
        def similar(a,b):
            return union_find.find(a) == union_find.find(b)

        for i in range(len(sentence1)):
            if not similar(sentence1[i], sentence2[i]):
                return False
        return True
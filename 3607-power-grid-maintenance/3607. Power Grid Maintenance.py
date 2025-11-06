class UnionFind:
    def __init__(self):
        self.parent = {}

    def union(self, x, y):
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 != p2:
            self.parent[p1] = p2

    def find(self, x):
        self.parent.setdefault(x, x)
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        union_find = UnionFind()
        for a, b in connections:
            union_find.union(a, b)
        adj = defaultdict(SortedList)
        keys = list(union_find.parent.keys())
        
        for i in range(1,c+1):
            adj[union_find.find(i)].add(i)

        offline = set()
  
        res = []
        for a,b in queries:
            if a == 1:
                if b not in offline:
                    res.append(b)
                    continue
                while adj[union_find.find(b)]:
                    if adj[union_find.find(b)][0] not in offline:
                        res.append(adj[union_find.find(b)][0])
                        break
                    else:
                        adj[union_find.find(b)].pop(0)
                else:
                    res.append(-1)
            else:
                offline.add(b)
        return res
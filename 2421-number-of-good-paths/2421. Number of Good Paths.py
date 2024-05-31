class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
    
    def find(self, i):
        while i != self.par[i]:
            self.par[i] = self.par[self.par[i]]
            i = self.par[i]
        return i
    
    def union(self, a, b):
        aRoot = self.find(a)
        bRoot = self.find(b)
        if aRoot == bRoot:
            return False
        if self.rank[aRoot] < self.rank[bRoot]:
            self.par[aRoot] = bRoot
            self.rank[bRoot] += self.rank[aRoot]
        else:
            self.par[bRoot] = aRoot
            self.rank[aRoot] += self.rank[bRoot]
        return True

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        valToIndex = defaultdict(list)
        for i, val in enumerate(vals):
            valToIndex[val].append(i)
        res = 0
        uf = UnionFind(len(vals))
        for val in sorted(valToIndex.keys()):
            for i in valToIndex[val]:
                for nei in adj[i]:
                    if vals[nei] <= vals[i]: 
                        uf.union(nei, i) #only union if value is less
            count = defaultdict(int)
            for i in valToIndex[val]:
                count[uf.find(i)] += 1
                res+=count[uf.find(i)]
            #for each disjoint set, how many vals does it contain 
        return res



        
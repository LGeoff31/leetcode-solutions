class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        
        self.parent[px] = py

class Solution:
    def exists(self, sorted_arr, val):
        idx = bisect_left(sorted_arr, val)
        if idx >= len(sorted_arr):
            return False 
        return sorted_arr[idx] == val

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = UnionFind()
        for u,v in allowedSwaps:
            uf.union(u, v)
        if not uf.parent:
            return sum(target[i] != source[i] for i in range(len(target)))

        dic = defaultdict(SortedList)

        for i in range(len(source)):
            root = uf.find(i)
            dic[root].add(source[i])

        print(uf.parent)
        print(dic)
        res = 0
        for i in range(len(source)):
            root = uf.find(i)
            valid_options = dic[root]
            if self.exists(valid_options, target[i]):
                valid_options.remove(target[i])
            else:
                res += 1
        
        return res
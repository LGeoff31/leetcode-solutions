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
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        union_find = UnionFind()
        dic = defaultdict(list)
        for a,b in synonyms:
            union_find.union(a,b)
        for key in union_find.parent:
            dic[union_find.find(key)].append(key)
        for key in dic:
            dic[key] = sorted(dic[key])
        
        words = text.split()
        n = len(words)

        res = []
        def dfs(i):
            if i == n:
                res.append(" ".join(words))
                return
            if words[i] in union_find.parent:
                par = union_find.find(words[i])
                for syn in dic[par]:
                    words[i] = syn
                    dfs(i+1)
            else:
                dfs(i+1)

        dfs(0)
        return res

        
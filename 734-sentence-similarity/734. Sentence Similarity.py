class Solution:
    def areSentencesSimilar(self, s1: List[str], s2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(s1)!=len(s2): return False
        d = defaultdict(set)
        for x,y in similarPairs:
            d[x].add(y)
            d[y].add(x)
        # d = {a:b for a,b in similarPairs}
        return all((s1[i]==s2[i] or (s1[i] in d and s2[i] in d[s1[i]]) or (s2[i] in d and s1[i] in d[s2[i]])) for i in range(len(s1)))
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        a = []
        dic = {}
        b = set()
        for p,w in items1:
            b.add(p)
        for p,w in items2:
            b.add(p)
        for elem in b:
            dic[elem] = 0
        for p,w in items1:
            dic[p] += w
        for p,w in items2:
            dic[p] += w
        for key in dic:
            a.append([key, dic[key]])
        return sorted(a)
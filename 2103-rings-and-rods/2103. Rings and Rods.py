class Solution:
    def countPoints(self, rings: str) -> int:
        dic = defaultdict(set)
        for i in range(1, len(rings), 2):
            dic[rings[i]].add(rings[i-1])
        return sum(len(dic[key]) == 3 for key in dic)
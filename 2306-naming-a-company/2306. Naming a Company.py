class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dic = defaultdict(set)
        for string in ideas:
            dic[string[0]].add(string[1:])
        res = 0
        print(dic)
        visited = set()
        for key1 in dic:
            for key2 in dic:
                if key1 == key2:
                    continue
                intersect = 0
                for w in dic[key1]:
                    if w in dic[key2]:
                        intersect+=1
                distinct1 = len(dic[key1]) - intersect
                distinct2 = len(dic[key2]) - intersect
                res+= (distinct1 * distinct2)
        return res
                
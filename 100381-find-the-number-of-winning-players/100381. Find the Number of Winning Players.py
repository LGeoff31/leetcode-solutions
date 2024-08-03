class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        dic = defaultdict(list)
        for x,y in pick:
            dic[x].append(y)
        res = 0
        print(dic)
        for i in range(10):
            if i in dic:
                for j in range(11):
                    if dic[i].count(j) > i:
                        res += 1
                        break
        return res
        
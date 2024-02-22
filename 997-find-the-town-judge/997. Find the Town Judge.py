class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        dic = {}
        for i in range(n):
            dic[i+1] = []

        for a, b in trust:
            dic[b].append(a)

        print(dic)
        for key in dic:
            if len(dic[key]) == n-1:
                valid = True
                for a in dic:
                    if key in dic[a]:
                        valid = False
                        break
                if valid: return key
        return -1



        
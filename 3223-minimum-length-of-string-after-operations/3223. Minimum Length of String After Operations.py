class Solution:
    def minimumLength(self, s: str) -> int:
        dic = defaultdict(list)
        for i, c in enumerate(s):
            dic[c].append(i)
        res = 0
        for key in dic:
            if len(dic[key]) % 2 == 1:
                res += 1
            else:
                res += 2
        return res
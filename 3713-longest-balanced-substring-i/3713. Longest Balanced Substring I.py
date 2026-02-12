class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        def check(dic):
            if min(dic.values()) == max(dic.values()):
                return sum(dic.values())
            return -1
        for i in range(len(s)):
            dic = defaultdict(int)
            for j in range(i, len(s)):
                dic[s[j]] += 1
                res = max(res, check(dic))


        return res
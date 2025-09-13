class Solution:
    def maxFreqSum(self, s: str) -> int:
        a,b = 0, 0
        dic=Counter(s)
        for v in ["a", "e", "i", "o", "u"]:
            if v in dic:
                a = max(a, dic[v])
        for key in dic:
            if key not in ["a", "e", "i", "o", "u"]:
                b = max(b, dic[key])
        return a+b
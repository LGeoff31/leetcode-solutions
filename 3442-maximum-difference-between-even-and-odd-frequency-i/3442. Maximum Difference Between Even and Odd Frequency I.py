class Solution:
    def maxDifference(self, s: str) -> int:
        dic = Counter(s)
        a,b = -1, 1e9
        for key in dic:
            if dic[key] % 2:
                a = max(a, dic[key])
            else:
                b = min(b, dic[key])
        return a-b
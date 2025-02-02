class Solution:
    def maxDifference(self, s: str) -> int:
        # odd - even
        dic = Counter(s)
        res = -1e9
        for key1 in dic:
            for key2 in dic:
                if dic[key1] % 2 == 1 and dic[key2] % 2 == 0:
                    res = max(res, dic[key1] - dic[key2])
        return res 
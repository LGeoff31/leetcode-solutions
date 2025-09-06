class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        min_freq = min(Counter(str(n)).values())
        res = 1e9
        a = Counter(str(n))
        for key in a:
            if a[key] == min_freq:
                res = min(res, int(key))
        return res

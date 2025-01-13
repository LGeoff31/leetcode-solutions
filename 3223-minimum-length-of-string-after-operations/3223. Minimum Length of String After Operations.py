class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        
        dic = Counter(s)
        res = 0
        freq = dic.values()
        for val in freq:
            if val%2:
                res += 1
            else:
                res +=2
        return res
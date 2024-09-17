class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a,b = Counter(s1.split()), Counter(s2.split())
        res = []
        for key in a:
            if key not in b and a[key] == 1:
                res.append(key)
        for key in b:
            if key not in a and b[key] == 1:
                res.append(key)
        return res
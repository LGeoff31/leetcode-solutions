class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v= sum(1 for c in s if c in {"a", "e", "i", "o", "u"})
        c = sum(1 for c in s if (c not in {"a", "e", "i", "o", "u"} and c.isalpha()))
        print(c)
        if c != 0:
            return floor(v / c)
        return 0
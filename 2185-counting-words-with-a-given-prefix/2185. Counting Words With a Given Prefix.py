class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if pref == word[:len(pref)]:
                res += 1
        return res
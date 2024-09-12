class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = []
        for word in words:
            b = set()
            for c in word:
                b.add(c)
            a.append(b)
        d = set()
        for c in allowed:
            d.add(c)
        count = 0
        for key in a:
            valid = True
            for c in key:
                if c not in d:
                    valid = False
                    break
            if valid:
                count += 1
        return count
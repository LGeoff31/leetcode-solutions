class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dic = defaultdict(int)
        for c in licensePlate:
            if c.isalpha():
                dic[c.lower()] += 1
        def valid(z):
            for key in dic:
                if key not in z or dic[key] > z[key]:
                    return False
            return True
        res = ""
        minLen = 1e9
        for word in words:
            z = Counter(word)
            if valid(z):
                if len(word) < minLen:
                    minLen = len(word)
                    res = word
        return res
        
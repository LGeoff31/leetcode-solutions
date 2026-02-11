class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a = Counter(words1)
        b = Counter(words2)
        res = 0
        for word in a:
            if a[word] == 1 and word in b and b[word] == 1:
                res += 1
        return res
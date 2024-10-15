class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        a = Counter(words)
        words = list(set(words))
        def match(subsequence):
            idx = 0
            for i in range(len(s)):
                if s[i] == subsequence[idx]:
                    idx += 1
                    if idx == len(subsequence): return True
            return idx == len(subsequence)
        res = 0
        for word in words:
            if match(word):
                res += a[word]
        return res
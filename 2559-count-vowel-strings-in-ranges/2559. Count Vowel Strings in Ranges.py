class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = []
        def valid(word):
            return word[0] in "aeiou" and word[-1] in "aeiou"
        for i, word in enumerate(words):
            if not prefix:
                if valid(word):
                    prefix.append(1)
                else:
                    prefix.append(0)
            else:
                if valid(word):
                    prefix.append(prefix[i-1] + 1)
                else:
                    prefix.append(prefix[i-1])
        res = []
        for start, end in queries:
            if start == 0:
                res.append(prefix[end])
            else:
                res.append(prefix[end] - prefix[start - 1])
        print(prefix)
        return res
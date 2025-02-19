class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # If any suffix of words[i] matches a prefix of words[j] such that i != j, then combine the two words
        words = set(words)
        lengths = set([len(word) for word in words])
        intervals = []
        for window in lengths:
            for i in range(len(s) - window+1):
                if s[i: i+window] in words:
                    intervals.append((i, i+window))
        intervals.sort(key=lambda x: (x[0], x[1]))
        merged = []
        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        res = list(s)
        for start, end in merged[::-1]:
            res.insert(end, "</b>")
            res.insert(start, "<b>")
        return "".join(res)
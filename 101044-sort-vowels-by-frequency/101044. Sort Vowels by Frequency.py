class Solution:
    def sortVowels(self, s: str) -> str:
        freq = defaultdict(int)
        occurence = {}
        
        for i, c in enumerate(s):
            if c in {"a", "e", "i", "o", "u"}:
                if c not in occurence:
                    occurence[c] = i
                freq[c] += 1

        a = [[freq, occurence[letter], letter] for letter, freq in freq.items()]
        a.sort(key = lambda x: (-x[0], x[1]))

        res = ""
        idx = 0
        for c in s:
            if c in {"a", "e", "i", "o", "u"}:
                if a[idx][0] >= 1:
                    res += a[idx][2]
                    a[idx][0] -= 1
                else:
                    idx += 1
                    res += a[idx][2]
                    a[idx][0] -= 1
            else:
                res += c
        return res
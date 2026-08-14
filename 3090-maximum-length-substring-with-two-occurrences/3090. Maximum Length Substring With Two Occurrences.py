class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        def valid(word):
            frequency_counter = Counter(word)
            return all(frequency_counter[c] <= 2 for c in frequency_counter)

        res = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                substring = s[i: j+1]
                if valid(substring):
                    res = max(res, j-i+1)
        return res
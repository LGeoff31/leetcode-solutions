class Solution:
    def numSplits(self, s: str) -> int:
        res = 0
        dic1 = Counter(s)
        dic2 = {}

        for letter in s:
            dic1[letter] -= 1
            if dic1[letter] == 0:
                del dic1[letter]
            dic2[letter] = 1 + dic2.get(letter, 0)
            res += len(dic1) == len(dic2)
        return res
        
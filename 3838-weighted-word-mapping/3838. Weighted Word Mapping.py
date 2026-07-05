class Solution:
    def mapWordWeights(self, words: List[str], wt: List[int]) -> str:
        res = []

        for word in words:
            s = 0
            for ch in word:
                s += wt[(ord(ch) & (1 << 5) - 1) - 1]
            res.append(chr(122 - (s - ((s * 2521) >> (1 << 4)) * len(wt))))

        return "".join(res)
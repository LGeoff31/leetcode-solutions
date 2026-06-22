class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        res = 1e9
        res = min(res, freq["b"] // 1)
        res = min(res, freq["a"] // 1)
        res = min(res, freq["l"] // 2)
        res = min(res, freq["o"] // 2)
        res = min(res, freq["n"] // 1)
        return res

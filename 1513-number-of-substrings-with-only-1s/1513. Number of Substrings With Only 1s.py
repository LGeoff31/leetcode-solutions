class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        curr = 0
        for c in s:
            if c == "1":
                curr += 1
            else:
                res += curr * (curr + 1) // 2
                curr = 0
        res += curr * (curr + 1) // 2
        return res % (10 ** 9 + 7)
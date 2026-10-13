class Solution:
    def minRotations(self, s: str) -> int:
        def dist(num1, num2):
            diff = max(num2, num1) - min(num1, num2)
            return min(diff, 10-diff)
        s = "0" + s
        res = 0
        for i in range(1, len(s)):
            res += dist(int(s[i]), int(s[i-1]))
            print(res)
        return res
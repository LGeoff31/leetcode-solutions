class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        lst = colors + colors
        dp = [1] * (2*n)
        for i in range(1, 2*n):
            if lst[i] != lst[i-1]:
                dp[i] = 1 + dp[i-1]
        res = 0
        for i in range(n):
            if dp[i] >= 3 or dp[i+n] >= 3:
                res += 1
        return res
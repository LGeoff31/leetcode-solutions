class Solution:
    def countSubstrings(self, s: str) -> int:
        # DP
        # Let's say we know a substirng is currently palindromic, let's expand 1 character to the left and right and if there equal, then boom
        # dp[i][j] = True if s[i:j] is palindromic otherwise False
        # Loop through this 2 dimensional dp grid and return the # of True's
        # We know dp[i][i] = True for 0 <= i < len(s)
        # For each i, we will say while (i-j, i+j) are equal, dp[i-j] = dp[i+j] = True, note that i-j >= 0 and i+j < len(s)
        # This will indeed find all palindromic substrings of odd length in O(n^2) time 
        # What about even length?
        # Run similar algorithm but now, the start will be dp[i][i+1] = True if s[i] == s[i+1], i+1 < len(s)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n):
            # Odd length
            j = 1
            while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
                dp[i-j][i+j] = True
                j += 1
            j = 1
            # Even length
            if i+1 < n and s[i] == s[i+1]:
                dp[i][i+1] = True
                while i-j >= 0 and i+1+j < n and s[i-j] == s[i+j+1]:
                    dp[i-j][i+j+1] = True
                    j += 1
        res = 0
        for i in dp:
            for j in i:
                res += j
        # print(dp)
        return res
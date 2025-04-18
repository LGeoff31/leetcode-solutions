class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        
        # A palindrome as a subsequence, seems a lot like DP
        # Since we can do a O(n^2) sol'n, I believe DP works
        # dp[i][j] = # palindromic subsequences from s[i: j+1]
        # btw j>=i
        # s = "bccb"
        """
             i
          0 1 2 3 
        0 1 0 0 0 
        1 2 1 0 0
        2 3   1 0
        3 6     1 

        if s[j] == s[i]:
            dp[i][j] = (j-i) + max(dp[i][j-1], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + s[j] is new character
        """
        n = len(s)
        dp=[[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] != s[j]:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                else:
                    ans = dp[i+1][j-1] * 2
                    left, right = i+1, j-1
                    while left <= right and s[left] != s[i]:
                        left += 1
                    while right >= left and s[right] != s[i]:
                        right -= 1
                    if left < right:
                        ans -= dp[left+1][right-1]
                    elif left == right:
                        ans += 1
                    else:
                        ans += 2
                    dp[i][j] = ans
        return dp[0][n-1] % MOD

        # def dfs(i, j):
        #     if j > i:
        #         return 0
        #     if i == j:
        #         return 1
            
        #     if s[i] == s[j]:
        #         ans = dfs(i+1, j-1) * 2
        #         left, right = i+1, j-1
        #         while left <= right and s[left] != s[i]:
        #             left += 1
        #         while right >= left and s[right] != s[i]:
        #             right -= 1
        #         if left < right:
        #             ans -= dfs(left+1, right - 1)
        #         elif left == right:
        #             ans += 1
        #         else:
        #             ans += 2
        #         return ans
        #     else:
        #         return dfs(i+1, j) + dfs(i, j-1) - dfs(i+1, j-1)

        # return dfs(0, n-1)



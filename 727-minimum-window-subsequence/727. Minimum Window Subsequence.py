class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # the 
        # ;et dp[j]pe = s be the largest index for which s[s: e+1] has T[:j] as a substring
        # s1 -> n, s2 -> m
        # return dp[m][n]

        # dp[i][j] = max starting point s1[:i+1], s2[:j+1]
        # minimize dp[-1][i] - i

        # O(nm)
        
        cols, rows = len(s1), len(s2)
        dp = [[-1] * cols for _ in range(rows)]
        if s1[0] == s2[0]:
            dp[0][0] = 0
        # dp[0][0] = s
        # fill first row
        for c in range(1, cols):
            if s2[0] == s1[c]:
                dp[0][c] = c
            else:
                dp[0][c] = dp[0][c-1]

        for r in range(1, rows):
            for c in range(1, cols):
                if s1[c] == s2[r]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = dp[r][c-1]
        # print(dp)
        start, minLen = 0, 1e9
        for c in range(cols):
            starting_idx = dp[-1][c]
            if starting_idx != -1 and c-starting_idx+1 < minLen:
                minLen = c-starting_idx+1
                start = starting_idx
        # print(res)
        return s1[start: start+minLen] if minLen != 1e9 else ""

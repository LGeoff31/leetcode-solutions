class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[False] * (len(s1)+2) for _ in range(len(s2)+2)]
        if len(s1) + len(s2) != len(s3): return False

        rows, cols = len(dp), len(dp[0])
        for c in range(1, cols - 1):
            dp[0][c] = s1[c-1]
        for r in range(1, rows - 1):
            dp[r][0] = s2[r-1]
        
        dp[-1][-1] = True
        for c in range(cols-2, 0, -1):
            if dp[-1][c+1] == True and dp[0][c] == s3[rows-2 + c-1]:
                dp[-1][c] = True
            else:
                dp[-1][c] = False
        for r in range(rows-2, 0, -1):
            if dp[r+1][-1] == True and dp[r][0] == s3[cols-2 + r-1]:
                dp[r][-1] = True
            else:
                dp[r][-1] = False
        print(dp)

        for r in range(rows-2, 0, -1):
            for c in range(cols-2, 0, -1):
                if (s3[r-1+c-1] == dp[r][0] and dp[r+1][c] == True) or (s3[r-1+c-1] == dp[0][c] and dp[r][c+1] == True):
                    dp[r][c] = True
        print(dp)
        return dp[1][1]


        
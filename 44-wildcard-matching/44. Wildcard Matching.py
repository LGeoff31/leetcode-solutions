class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows, cols = len(s), len(p)
        dp = [[False] * (cols+1) for _ in range(rows+1)]
        dp[0][0] = True
        # print("cols", cols)
        #fill in first row
        for c in range(1, cols+1):
            if p[c-1] == "*":
                if c-1 == 0:
                    dp[0][c] = True
                else:
                    dp[0][c] = dp[0][c-1]
                # dp[0][c] = 
            else:
                dp[0][c] = False
            # dp[0][c] = p[c-1] == "*"
        
        #fill in first column
        for r in range(1, rows+1):
            dp[r][0] = False
        
        #bottom up approach working left -> right, top -> down
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if p[c-1] == s[r-1] or p[c-1] == "?":
                    dp[r][c] = dp[r-1][c-1]
                elif p[c-1] == "*":
                    dp[r][c] = dp[r-1][c] or dp[r][c-1]
                else:
                    dp[r][c] = False
        # print(dp)
        return dp[-1][-1]
                
        
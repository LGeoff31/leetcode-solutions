class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        # Graph problem: Each cell is connected to each of its at most 8 neighbors 
        # 4 cases, horz, ver, dia, anti-dia
        # dp[r][c][1...4] vertical horz diag anti-dia
        # O(8rc)
        dp = [[[0, 0, 0, 0] for _ in range(cols)] for l in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    dp[r][c] = [1,1,1,1]
        print(dp, 'ad')
        print('')
        # run left -> rihgt, top -> bottom
        for r in range(rows):
            for c in range(cols):
                # Vertcal
                up, down = 0, 0
                if r-1>=0 and mat[r-1][c] == 1: up = dp[r-1][c][0]
                # if r+1<rows and mat[r+1][c] == 1: down = dp[r+1][c][0]
                dp[r][c][0]=mat[r][c]+up+down
                # Horz
                left, right = 0, 0
                if c-1>=0 and mat[r][c-1] == 1: left = dp[r][c-1][1]
                # if c+1<cols and mat[r][c+1] == 1: right = dp[r][c+1][1]
                dp[r][c][1]=mat[r][c]+left+right
                # Diag
                a,b = 0,0 
                if c+1<cols and r-1>=0 and mat[r-1][c+1] == 1: a = dp[r-1][c+1][2]
                # if c-1>=0 and r+1<rows and mat[r+1][c-1] == 1: b = dp[r+1][c-1][2]
                dp[r][c][2]=mat[r][c]+a+b
                # Anti-diag
                a,b = 0, 0
                if c-1>=0 and r-1>=0 and mat[r-1][c-1] == 1: a = dp[r-1][c-1][3]
                # if c+1<cols and r+1<rows and mat[r+1][c+1] == 1: d = dp[r+1][c+1][3]
                dp[r][c][3]=mat[r][c]+a+b
        print(dp)
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, max(dp[r][c]))
        return res
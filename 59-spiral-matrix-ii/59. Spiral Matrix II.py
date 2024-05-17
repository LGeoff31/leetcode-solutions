class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        idx = 1
        l, r = 0, n-1
        t, d = 0, n-1

        horz_increasing = True
        vert_increasing = True

        dp = [[0] * n for _ in range(n)]


        while l <= r and t <= d:
            for i in range(l, r+1):
                dp[t][i] = idx
                idx+=1
            t+=1
            for i in range(t, d+1):
                dp[i][r] = idx
                idx+=1
            r -= 1
            if l > r or t > d: break
            for i in range(r, l-1, -1):
                dp[d][i] = idx
                idx+=1
            d -=1
            for i in range(d, t-1, -1):
                dp[i][l] = idx
                idx+=1
            l+=1
        return dp


        
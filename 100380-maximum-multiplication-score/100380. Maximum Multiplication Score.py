class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dp = [[-float('inf')] * n for _ in range(4)]
        
        dp[0][0] = a[0] * b[0] # dp[i[k] = max score using first i elements of array a and first k elements of array b
        for k in range(1, n):
            dp[0][k] = max(dp[0][k-1], a[0] * b[k])
        
        for i in range(1, 4):
            for k in range(i, n):
                dp[i][k] = max(dp[i][k-1], dp[i-1][k-1] + a[i] * b[k])
        
        return max(dp[3][3:])

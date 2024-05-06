class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1


        for i in range(2, n+1):
            acc = 0
            for j in range(1, i+1):
                left = j-1
                right = i-j
                acc += max(dp[left] * dp[right], max(dp[left], dp[right]))
            dp[i] = acc


        return dp[n]
        
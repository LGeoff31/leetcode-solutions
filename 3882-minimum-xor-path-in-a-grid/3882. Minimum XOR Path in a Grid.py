class Solution:
    def minCost(self, A: list[list[int]]) -> int:
        dp = [set()] * len(A[0])
        dp[0] = set([0])
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                prev = dp[j].union(dp[j - 1]) if j else dp[j]
                dp[j] = set(x ^ A[i][j] for x in prev)                

        return min(dp[-1]) 
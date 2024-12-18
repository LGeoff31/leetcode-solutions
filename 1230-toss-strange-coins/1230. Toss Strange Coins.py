class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        if target == 0: 
            res = 1
            for num in prob:
                res *= 1-num 
            return res
        dp = [[0]*(target+1) for _ in range(len(prob))] #dp[i][j] = j heads at ith position
        dp[0][0] = 1-prob[0]
        dp[0][1] = prob[0]
        for i in range(1, len(prob)):
            dp[i][0] = dp[i-1][0] * (1-prob[i])
            for j in range(1, min(i+2,1+target)):
                if i >= j:
                    dp[i][j] = (dp[i-1][j]*(1-prob[i])) + (dp[i-1][j-1] * prob[i])
                else:
                    dp[i][j] = (dp[i-1][j-1] * prob[i])
        # print(dp)
        return dp[-1][target]
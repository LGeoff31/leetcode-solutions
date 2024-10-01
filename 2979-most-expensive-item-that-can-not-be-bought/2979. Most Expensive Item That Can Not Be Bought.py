class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        n = primeOne * primeTwo - 1
        dp = [0] * n
        dp[primeOne] = 1
        dp[primeTwo] = 1
        for i in range(2, n):
            if dp[i] == 1: continue
            if dp[i - primeOne] == 1 or dp[i - primeTwo] == 1:
                dp[i] = 1
        for i in range(len(dp) -1, -1, -1):
            if dp[i] == 0:
                return i
        print(dp)
        return primeOne * primeTwo - 1
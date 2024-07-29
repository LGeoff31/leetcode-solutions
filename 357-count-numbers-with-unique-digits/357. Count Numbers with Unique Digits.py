class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0] * 9
        dp[0] = 1
        dp[1] = 10

        def length_number(n):
            # 1 -> 10
            # 2 -> 9x9 = 81
            # 3 -> 9x9x8 = 648
            if n == 1: return 10
            return 9 * factorial(9) // factorial(9-n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + length_number(i)


        return dp[n]
        
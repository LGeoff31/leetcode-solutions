class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * 1001
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        dp[5] = 5

        def is_prime(num):
            for i in range(2, 1 + floor(sqrt(num))):
                if num % i == 0:
                    return False
            return True
        for i in range(6, 1001):
            if is_prime(i):
                dp[i] = i
            else:
                idx = 2
                while i % idx != 0:
                    idx += 1
                if i == 6:
                    print(idx)
                dp[i] = i // (i // idx) + dp[i // idx]
        # print(dp)
        return dp[n]
        
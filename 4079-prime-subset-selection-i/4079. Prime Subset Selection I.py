class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        """
        [1,2,3,4,5,6,7,8,9,10]
        """
        is_prime = [True] * (n+1)
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(sqrt(n) + 1)):
            if is_prime[i]:
                for multiple in range(i * i, n+1, i):
                    is_prime[multiple] = False 
        res = []
        curr = 0
        for i in range(1, n+1):
            if is_prime[i]:
                if curr + i <= s:
                    curr += i
                    res.append(i)
                else:
                    break
        return res

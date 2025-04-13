class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # 10^14 -> 10^15 is a lot of numbers to loop through
        # Note that odd idicies must fall in 2,3,5,7
        # Combinatorics problem

        # n = 4
        # [2,4,6,8][2,3,5,7][0,2,4,6,8][2,3,5,7]
        res = 1
        odd = n%2
        remain = n-1
        odd_times = ceil(remain / 2)
        even_times = remain-odd_times
        res *= pow(5,odd_times, MOD)
        res *= pow(4, even_times, MOD)
    
        res *= 4 + odd
        return res % MOD
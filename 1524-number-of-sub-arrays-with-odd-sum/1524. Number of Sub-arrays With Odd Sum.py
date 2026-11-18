class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        """
        DP??
        dp[i][0/1] -> # of subarrays that are odd/even ending with i
        [1, 1, 1] -> 

        dp = [
            [0, 1],
            [1, 1],
            [1. 2],
        ]
        []
        """
        seen_even_sum_subarrays = 0
        seen_odd_sum_subarrays = 0
        res = 0
        MOD = 10 ** 9 + 7
        current_sum = 0
        for num in arr:
            current_sum += num

            if current_sum % 2 == 1:
                res += seen_even_sum_subarrays + 1
                seen_odd_sum_subarrays += 1
            else:
                res += seen_odd_sum_subarrays
                seen_even_sum_subarrays += 1
        return res % MOD

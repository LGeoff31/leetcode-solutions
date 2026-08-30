class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        """
        Observations, when you floor a even number its even
        when you floor a odd number its even
        multiplying number by 2 will produce even
        so whenever you apply operation, the number will persist even

        when will it be impossible ? 
        if sum > len(nums) and 

        since all divisions can only occur afte rmultiplications
        that's only handy if you want num to be lower than its current value

        6: 1, 3, 6, 12, 24, 48, ...
        3: 1, 3, 6, 12, ...
        4: 1,2,4,8,16

        all nums are positive and sum < 5000, so the options for each num are limited to log(5000) = 2^2 * 2^10 = 12 options
        100 * 12 = 1200 total possible options

        at each value, we can do a take or dont take, over all 12 options through, O(12n) ?? 
        """
        @cache
        def get_options(num):
            rising_options = []
            num_copy = num // 2
            while num <= 5000:
                rising_options.append(num)
                num *= 2

            descending_options = []
            while num_copy > 0:
                descending_options.append(num_copy)
                num_copy //= 2
                
            return tuple(rising_options), tuple(descending_options)

        dp = [1e9] * (sum + 1)
        dp[0] = 0

        for i in range(len(nums) -1, -1, -1):
            new_dp = [1e9] * (sum + 1)
            rising, descending = get_options(nums[i])
            for s in range(sum + 1):
                best = dp[s]
                for idx, v in enumerate(rising):
                    if v <= s and dp[s-v] != 1e9:
                        best = min(best, dp[s-v] + idx)
                for idx, v in enumerate(descending):
                    if v <= s and dp[s-v] != 1e9:
                        best = min(best, dp[s-v] + idx + 1)
                new_dp[s] = best
            dp = new_dp
        return dp[sum] if dp[sum] != 1e9 else -1
        # @cache
        # def dfs(i, current_sum): #O(100 * 5000 * 12)
        #     if current_sum == 0:
        #         return 0

        #     if current_sum < 0 or i >= len(nums):
        #         return 1e9

        #     res = 1e9
            
        #     # TAKE
        #     rising_options, descending_options = get_options(nums[i])
        #     for idx in range(len(rising_options)):
        #         res = min(res, dfs(i+1, current_sum - rising_options[idx]) + (idx))

        #     for idx in range(len(descending_options)):
        #         res = min(res, dfs(i+1, current_sum - descending_options[idx]) + (idx + 1))
                
        #     # DONT TAKE
        #     res = min(res, dfs(i+1, current_sum))

        #     return res
            
        # res = dfs(0, sum)
        # return res if res != 1e9 else -1
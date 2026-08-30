class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        """
        i believe the only addition is every single nums can be 1 .. 2^12 now bc you can
        always divide until 1, then multiply out by 2
        
        """
        @cache
        def get_options(num):
            options = {}
            base = num
            h = 0
            while True:
                if base == 0:
                    if h < options.get(0, float('inf')):
                        options[0] = h
                    break
                val = base 
                d = 0
                while val <= 5000:
                    cost = h + d
                    if cost < options.get(val, float('inf')):
                        options[val] = cost
                    val *= 2
                    d += 1

                base //= 2
                h += 1
            return options
                

        dp = [1e9] * (sum + 1)
        dp[0] = 0

        for i in range(len(nums) -1, -1, -1):
            new_dp = [1e9] * (sum + 1)
            options = get_options(nums[i])

            for s in range(sum + 1):
                best = dp[s]
                for v, cost in options.items():
                    if v <= s and dp[s-v] != 1e9:
                        best = min(best, dp[s-v] + cost)
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
class Solution:
    def jump(self, nums: List[int]) -> int:
        if nums[0] == 0: return 0
        if len(nums) == 1: return 0

        dp = [1e9] * len(nums)
        #dp[i] represents the minimum amount steps to get there

        #[1,3,4,5,2,6]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, len(nums)): #O(N)
            for j in range(i): #O(N)
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j]+1)


        print(dp)
        return dp[-1]


     
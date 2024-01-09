class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return max(nums)
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums)
        # one dp with the first character and not the last
        # one dp with the secound character and the last
        # max(dp1[-1], dp2[-1])
        dp1 = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)-1):
            dp1.append(0)
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
        dp2 = [0, nums[1], max(nums[2], nums[1])]

        for j in range(3, len(nums)):
            dp2.append(0)
            dp2[j] = max(dp2[j-2] + nums[j], dp2[j-1])
        print("dp1", dp1)
        print("dp2", dp2)

        return max(dp1[-1], dp2[-1])

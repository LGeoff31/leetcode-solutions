class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # c <num a+b
        nums.sort()
        res = 0
        for i in range(len(nums) -1, -1, -1):
            for j in range(i-1, 0, -1):
                if nums[j] + nums[j-1] > nums[i]:
                    return nums[j] + nums[j-1] + nums[i]
                    # res = max(res, nums[j] + nums[j-1] + nums[i])
        return res
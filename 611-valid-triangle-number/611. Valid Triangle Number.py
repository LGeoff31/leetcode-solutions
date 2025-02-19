class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = nums[i]
                b = nums[j]
                # if bisect_left(nums, min(a,b)) != 0:
                res += max(bisect_left(nums, a + b) - (j+1),0)
        return max(res,0)
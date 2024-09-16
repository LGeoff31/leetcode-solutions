class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n

        l, r = 0, 2*k

        if len(nums) <= r:
            return res 
        if k == 0:
            return nums
        first_sum = sum(nums[l:r+1]) - nums[r]

        for i in range(k, len(nums) - k):
            first_sum += nums[r]
            res[i] = first_sum // (2*k+1)
            first_sum -= nums[l]
            l += 1
            r += 1
        return res
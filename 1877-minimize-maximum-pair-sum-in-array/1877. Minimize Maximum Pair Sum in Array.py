class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        res = []
        nums.sort()
        
        n = len(nums)
        for i in range(len(nums) // 2):
            res.append(nums[i] + nums[n-i-1])
        print(res)        
        return max(res)
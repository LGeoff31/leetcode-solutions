class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path):
            if not nums:
                res.append(path)
            
            for i in range(len(nums)):
                backtrack(nums[0:i] + nums[i+1: ], path + [nums[i]])

        res = []
        backtrack(nums, [])
        return res
        

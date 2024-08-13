class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        nums.sort()
        def dfs(i, subset):
            if sum(subset) == target:
                res.append(subset.copy())
                return

            if sum(subset) > target or i >= len(nums):
                return
            #include number
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            #dont include number
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subset)
        dfs(0, [])
        return res

            
        
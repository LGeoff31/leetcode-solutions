class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # If find x that work, the gaps between adds 2^gap

        res = 0
        target = 0
        target = 0

        for num in nums:
            target |= num
        print(target)
        @cache
        def dfs(i, curr):
            if i == len(nums):
                return target == curr
            res = 0
            # Take num
            res += dfs(i+1, curr | nums[i])

            # Don't take
            res += dfs(i+1, curr)

            return res
        return dfs(0, 0)

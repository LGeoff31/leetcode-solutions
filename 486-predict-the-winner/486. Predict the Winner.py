class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, j):
            if i > j: 
                return 0
            a = nums[i] + min(dfs(i+1, j-1), dfs(i+2, j))
            b = nums[j] + min(dfs(i+1, j-1), dfs(i, j-2))
            return max(a,b)
    
        p1 = dfs(0, len(nums) - 1)
        return p1 >= sum(nums) - p1
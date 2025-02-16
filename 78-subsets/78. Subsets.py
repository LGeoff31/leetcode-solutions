class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(i, arr):
            if i == len(nums):
                self.res.append(arr)
                return
            print(i)
            dfs(i+1, arr+[nums[i]])
            dfs(i+1, arr)
        dfs(0, [])
        return self.res
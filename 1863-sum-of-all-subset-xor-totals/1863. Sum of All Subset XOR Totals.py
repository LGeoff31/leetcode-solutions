class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def XOR(arr):
            res = 0
            for n in arr:
                res ^= n
            return res
        
        self.subsequences = []
        def dfs(idx, arr):
            if idx == len(nums):
                self.subsequences.append(arr)
                return
        
            dfs(idx+1, arr + [nums[idx]])
            dfs(idx+1, arr)
        

        dfs(0, [])
        res = 0
        for arr in self.subsequences:
            res += XOR(arr)
        # print(self.subsequences)
        return res
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.longest_valid = []
        visited = set()
        # O()
        def dfs(idx, arr): #O(2^n)
            if idx == len(nums):
                # if len(arr) > len(self.longest_valid):
                if len(arr) > 1 and tuple(arr) not in visited:
                    visited.add(tuple(arr)) 
                    self.longest_valid.append(arr)
                return 
            
            if arr and nums[idx] >= arr[-1]:
                dfs(idx+1, arr + [nums[idx]])
            if not arr:
                dfs(idx+1, arr + [nums[idx]])
            dfs(idx+1, arr)
        dfs(0, [])

        print(self.longest_valid)
        return self.longest_valid
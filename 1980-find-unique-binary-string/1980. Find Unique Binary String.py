class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        self.res = ""
        def dfs(string):
            if len(string) == n:
                if string not in nums:
                    self.res = string
                return
            
            dfs(string + "1")
            dfs(string + "0")
        dfs("")
        return self.res


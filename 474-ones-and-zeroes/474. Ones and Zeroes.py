class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        lst = [[a.count("0"), a.count("1")] for a in strs]
        @cache
        def dfs(zeros, ones, idx):
            if zeros < 0 or ones < 0:
                return -1e9
            if idx == len(strs):
                return 0
            
            # Take or don't take situation
            return max(1 + dfs(zeros - lst[idx][0], ones - lst[idx][1], idx+1), dfs(zeros, ones, idx+1))
        
        return dfs(m, n, 0)
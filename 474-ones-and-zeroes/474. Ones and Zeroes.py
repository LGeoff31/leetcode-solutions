class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dfs(i, zeros, ones):
            if not (zeros <= m and ones <= n):
                return -1e9
            
            if i == len(strs):
                return 0
            s = strs[i]
            return max(1 + dfs(i+1, zeros + s.count("0"), ones + s.count("1")), dfs(i+1, zeros, ones))
        return dfs(0, 0, 0)
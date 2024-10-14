class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        m,n = len(source), len(pattern)
        s = set(targetIndices)
        @lru_cache(None)
        def dfs(i, j): # Returns maximum number removals from indexes i and j
            if i == m:
                if j == n: return 0
                else: return -1e9
            
            if j == n:
                return int(i in s) + dfs(i+1, j)
            
            res = int(i in s) + dfs(i+1, j) # No take character 
            if source[i] == pattern[j]:
                res = max(res, dfs(i+1, j+1)) # Take character
            return res
        res = dfs(0, 0)
        dfs.cache_clear()
        return res if res != -1e9 else 0

            

            
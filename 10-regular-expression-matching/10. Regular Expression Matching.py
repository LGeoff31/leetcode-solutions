class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if i >= len(s) and j >= len(p): return True
            if j >= len(p): return False 

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j+1) < len(p) and p[j+1] == "*":
                return dfs(i, j+2) or (match and dfs(i+1, j))
            if match:
                return dfs(i+1, j+1)
            return False
        return dfs(0, 0)
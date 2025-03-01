class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j): # dfs(2, 0)
            if i == len(s) and j == len(p):
                return True
            if i > len(s) or j > len(p):
                return False
            if j == len(p):
                return False
            if i == len(s) and (j == len(p) - 1 or p[j+1] != "*"):
                return False
            print(i, j)
            if j+1 < len(p) and p[j+1] == "*":
                # Branch
                res = dfs(i, j+2)
                print(res)
                if (i < len(s) and p[j] == s[i]) or p[j] == ".":
                    res = res or dfs(i+1, j)
                print(i, j, res)
                return res
            elif p[j] == ".":
                return dfs(i+1, j+1)
            else:
                if p[j] != s[i]:
                    return False
                return dfs(i+1, j+1)
            
        return dfs(0, 0)
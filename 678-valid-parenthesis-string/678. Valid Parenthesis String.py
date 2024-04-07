class Solution:
    def checkValidString(self, s: str) -> bool:
        if abs(s.count("(") - s.count(")")) > s.count("*"): return False
        @cache
        def dfs(idx, counter):
            if idx == len(s):
                if counter == 0: return True
                else: return False
            if counter < 0: return False
            
            res = False
            if s[idx] == "(":
                res = res or dfs(idx+1, counter+1)
            elif s[idx] == ")":
                res = res or dfs(idx+1, counter-1)
            else:
                #3 cases
                res = res or dfs(idx+1, counter-1) or dfs(idx+1, counter+1) or dfs(idx+1, counter)
            return res

        return dfs(0,0)
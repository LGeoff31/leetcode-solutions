class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def dfs(open, close, curr):
            if open == close == n:
                self.res.append(curr)
                return
            if open > n:
                return

            if open == close:
                dfs(open+1, close, curr + "(")
            else:
                dfs(open, close+1, curr + ")")
                dfs(open+1, close, curr + "(")
        dfs(0, 0, "")
        return self.res


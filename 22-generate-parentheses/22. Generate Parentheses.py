class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def dfs(o, c, string):
            if o == c and o+c == 2*n:
                res.append(string)
            
            if o < n:
                dfs(o+1, c, string + "(")
            
            if c < o:
                dfs(o, c+1, string + ")")
        dfs(0, 0, "")
        return res
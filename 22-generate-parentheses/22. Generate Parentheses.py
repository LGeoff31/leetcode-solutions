class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def valid(expr):
            stack = []
            for c in expr:
                if c == "(":
                    stack.append("(")
                else:
                    if stack: stack.pop()
                    else: return False
            return len(stack) == 0

        def dfs(_in, out, expr):
            nonlocal res
            if _in == n and out == n:
                if valid(expr):
                    res.append(expr)
            if _in > n or out > n:
                return 
            
            dfs(_in+1, out, expr + "(")
            dfs(_in, out+1, expr + ")")
        
        dfs(0, 0, "")
        return res

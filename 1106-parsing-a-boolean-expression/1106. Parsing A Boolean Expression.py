class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parseArguments(expr):
            # This function will correctly parse arguments even with nested expressions
            result = []
            balance = 0
            current = []
            for char in expr:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                if char == ',' and balance == 0:
                    result.append(''.join(current))
                    current = []
                else:
                    current.append(char)
            result.append(''.join(current))  # Append the last expression
            return result
    

        def dfs(expr):
            if len(expr) == 0:
                return False
            if len(expr) == 1:
                return expr == "t"
            if expr[0] == "!":
                return not dfs(expr[2:-1])
            if expr[0] == "&":
                lst = parseArguments(expr[2: -1])
                res = True
                for sub in lst:
                    res = res and dfs(sub)
                return res
            if expr[0] == "|":
                lst = parseArguments(expr[2:-1])
                res = False
                for sub in lst:
                    res = res or dfs(sub)
                return res

        return dfs(expression)

        
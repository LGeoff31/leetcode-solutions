class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def valid_brackets(string):
            stack = []
            for char in string:
                if char == ")":
                    if not stack:
                        return False 
                    stack.pop()
                else:
                    stack.append(char)
            return not stack
        def dfs(string):
            if string.count(")") > string.count("("):
                return 
            if len(string) > 2*n:
                return
            if len(string) == 2*n:
                if valid_brackets(string):
                    print('string', string)
                    self.res.append(string)

            dfs(string + "(")
            dfs(string + ")")

        dfs("(")

        return self.res
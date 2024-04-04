class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == ")":
                res = max(res, len(stack))
                stack.pop()        
        return res

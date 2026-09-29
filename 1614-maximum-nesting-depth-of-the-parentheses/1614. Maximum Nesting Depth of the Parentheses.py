class Solution:
    def maxDepth(self, s: str) -> int:
        # consecutive closing )
        res = 0
        temp = 0
        stack = []

        for c in s:
            if c == "(":
                temp = 0
                stack.append(c)
            elif c == ")":
                temp += 1
                stack.pop()
            res = max(res, temp + len(stack))
        
        return res



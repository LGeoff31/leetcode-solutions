class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append([")", i])
            elif s[i] == "(":
                stack.append(["(", i])
        res = ""
        c = set([b for a,b in stack])
        for i in range(len(s)):
            if i not in c:
                res+=s[i]
        return res

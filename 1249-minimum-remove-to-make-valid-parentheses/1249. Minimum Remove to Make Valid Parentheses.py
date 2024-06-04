class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        stack = []
        bad_indicies = []
        lastest_open_bracket_indicies = []

        for i in range(len(s)):
            if s[i] == ")":
                if not stack:
                    bad_indicies.append(i)
                else:
                    stack.pop() #stack will only be popping a (
            elif s[i] == "(":
                stack.append("(")
                lastest_open_bracket_indicies.append(i)
        print("bad", bad_indicies)
        print(stack, lastest_open_bracket_indicies)
        if stack:
            iters = len(stack)
            backwards = lastest_open_bracket_indicies[::-1]
            for i in range(iters):
                bad_indicies.append(backwards[i])

        bad_indicies = set(bad_indicies)
        print(bad_indicies)
        for i in range(len(s)):
            if i not in bad_indicies:
                res+=s[i]
        return res
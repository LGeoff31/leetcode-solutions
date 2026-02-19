class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ["1"] * len(s)
        stack = []

        for i in range(len(s)):
            if s[i] == ")":
                if not stack:
                    continue
                idx = stack.pop()
                res[idx] = "("
                res[i] = ")"
            elif s[i] == "(":
                stack.append(i)
            else:
                res[i] = s[i]
        print(res)
        final_res = ""
        for c in res:
            if c != "1":
                final_res += c
        return final_res
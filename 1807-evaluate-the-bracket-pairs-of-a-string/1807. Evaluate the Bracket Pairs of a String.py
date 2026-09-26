class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        res = ""
        curr = ""
        dic = {key: value for key, value in knowledge}

        open_brace = False 
        for i in range(len(s)):
            if s[i] == "(":
                open_brace = True
                continue 

            if s[i] == ")":
                open_brace = False
                res += dic[curr] if curr in dic else "?"
                curr = ""
            elif open_brace:
                curr += s[i]
            else:
                res += s[i]

        return res
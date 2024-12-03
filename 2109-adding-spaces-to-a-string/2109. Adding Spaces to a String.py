class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        idx = 0
        for i in range(len(s)):
            if idx < len(spaces) and i == spaces[idx]:
                res += " "
                idx += 1
            res += s[i]

        return res
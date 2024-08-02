class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for letter in address:
            if letter == ".":
                res += "[.]"
            else:
                res += letter
        return res
        
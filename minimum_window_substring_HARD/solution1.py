class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_substring = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                valid = True
                for char in t:
                    if char not in substring:
                        valid = False
                    if t.count(char) > substring.count(char):
                        valid = False
                if valid:
                    min_substring = substring
        return min_substring

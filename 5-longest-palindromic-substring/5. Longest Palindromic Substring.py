class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        max_string = ""
        max_len = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    if len(substring) > max_len:
                        max_string = substring
                        max_len = len(substring)
        if len(max_string) < 1:
            return s[0]
        return max_string
        
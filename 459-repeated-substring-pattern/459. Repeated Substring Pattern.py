class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)):
            substring = s[:i+1]
            if len(s) % len(substring) != 0 or len(substring) == len(s):
                continue
            if substring * (len(s) // len(substring)) == s:
                return True
        return False
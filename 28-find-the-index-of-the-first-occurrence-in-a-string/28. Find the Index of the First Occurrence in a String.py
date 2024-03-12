class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)-len(needle)+1):
            sub_string = haystack[i:i+len(needle)]
            if sub_string == needle:
                return i
        return -1
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_substring = "a" * 10e5
        for char in t:
            if t.count(char) > s.count(char):
                return ""
        left, right = 0, 0
        while right < len(s):
            substring = s[left:right+1]
            valid = True
            for char in t:
                if t.count(char) > substring.count(char):
                    valid = False
                if char not in substring:
                    valid = False
            if valid:
                if len(min_substring) > len(substring):
                    min_substring = substring
                left += 1
            else:
                right += 1
        return min_substring

class Solution:
    def makePalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        diff = 0
        while l < r:
            diff += s[l] != s[r]
            l += 1
            r -= 1
        return diff == 1 or diff == 2 or diff == 0
        # Change 1 character


        # Change 2 character

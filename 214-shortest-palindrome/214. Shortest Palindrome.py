class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s: return ""

        def isPalindrome(string):
            return string == string[::-1]
        
        idx = -1
        for i in range(len(s), -1, -1):
            if isPalindrome(s[: i]):
                idx = i 
                break 
        print(idx)
        return s[idx:][::-1] + s[: idx] + s[idx:]
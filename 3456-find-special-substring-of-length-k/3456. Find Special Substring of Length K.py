class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s) - k + 1):
            window = s[i: i + k]
            print(window)
            if len(Counter(window)) == 1 and (i == 0 or s[i-1] != s[i]) and (i+k==len(s) or s[i+k] != s[i]):
                return True
        return False
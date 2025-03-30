class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        arr1 = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s) + 1)]
        arr2 = [t[i:j] for i in range(len(t)) for j in range(i+1, len(t) + 1)]
        print(arr1)
        print(arr2)
        def isPalindomre(string):
            return string == string[::-1]
        res = 0
        for substring1 in arr1:
            for substring2 in arr2:
                if isPalindomre(substring1): res = max(res, len(substring1))
                if isPalindomre(substring2): res = max(res, len(substring2))
                if isPalindomre(substring1 + substring2):
                    res = max(res, len(substring1 + substring2))
        return res
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                print(substring)
                if substring.count("0") <= k or substring.count("1") <= k:
                    res += 1
        return res
        
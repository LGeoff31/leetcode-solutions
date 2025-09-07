class Solution:
    def minOperations(self, s: str) -> int:
        no_a = ""
        for c in s:
            if c != "a":
                no_a += c
        res = 0
        print(ord('y') - ord('a'))
        for c in no_a:
            res = max(res, 26 - (ord(c) - ord('a')))

        return res
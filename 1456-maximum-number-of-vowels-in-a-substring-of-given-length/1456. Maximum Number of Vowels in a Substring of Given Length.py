class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", 'e', 'i', 'o', 'u'}

        count = 0
        lastIdx = 0
        print(len(s))

        for i in range(k):
            if s[i] in vowels: count += 1
        res = count
        for i in range(k, len(s)): #O(n)
            if s[i] in vowels: count += 1
            if s[lastIdx] in vowels: count -= 1
            lastIdx += 1
            res = max(res, count)

        return res

        
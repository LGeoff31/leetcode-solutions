class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L = [-1] * 26
        for i,c in enumerate(needle):
            L[ord(c) - ord('a')] = i
        n, m = len(haystack), len(needle)
        i, j = m-1, m-1
        while i < len(haystack):
            if haystack[i] == needle[j]:
                if j == 0:
                    return i
                j -= 1
                i -= 1
            else:
                i = i + (m-1) - min(L[ord(haystack[i])-ord("a")], j-1)
                j = m-1
            print(i,j)

        return -1
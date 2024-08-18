class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        a = {chr(65 + i) : (i+1) for i in range(26)}
        return sum(a[columnTitle[i]] * (26 ** (len(columnTitle) - i - 1)) for i in range(len(columnTitle)))
        
class Solution:
    def findValidPair(self, s: str) -> str:
        dic = Counter(s)
        for i in range(1, len(s)):
            first, second = int(s[i-1]), int(s[i])
            if first != second and dic[str(first)] == first and dic[str(second)] == second:
                return str(first) + str(second)
        return ""
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dic = defaultdict(int)
        streak = 0
        for i in range(len(s)):
            streak = streak + 1 if ((ord(s[i-1])-96) % 26) == ord(s[i]) - 97 else 1
            dic[s[i]] = max(dic[s[i]], streak)
        return sum(dic.values())
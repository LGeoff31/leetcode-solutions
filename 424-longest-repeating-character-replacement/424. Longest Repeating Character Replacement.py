class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_substring = 0
        left = 0
        dic = {}
        dic[s[left]] = 1
        for right in range(1, len(s)):
            if s[right] in dic:
                dic[s[right]] += 1
            else:
                dic[s[right]] = 1
            while sum(dic.values()) - max(dic.values()) > k:
                dic[s[left]] -= 1
                left += 1
            
            max_substring = max(max_substring, sum(dic.values()))
        return max_substring

                





        
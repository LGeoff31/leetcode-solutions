class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = -1e9
        for i in range(len(s)):
            seen = {s[i]}
            count = 1
            for j in range(i+1, len(s)):
                if s[j] in seen:
                    break
                count += 1
                seen.add(s[j])
            max_count = max(max_count, count)
        return max_count

        
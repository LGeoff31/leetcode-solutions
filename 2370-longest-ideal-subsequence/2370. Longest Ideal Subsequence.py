class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        lst = []
        for i in range(len(s)):
            lst.append(ord(s[i]) - ord("a"))
        
        m = defaultdict(int)
        dp = [1 for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(max(0, lst[i] - k), min(25, lst[i] + k) + 1):
                if j not in m:
                    continue
                if m[j] + 1 > dp[i]:
                    dp[i] = m[j] + 1
            m[lst[i]] = max(m[lst[i]], dp[i])

        return max(dp)

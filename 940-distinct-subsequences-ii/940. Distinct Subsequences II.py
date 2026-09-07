class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * (len(s))
        dp[0] = 1
        MOD = 10 ** 9 + 7
        seen_characters = {s[0] : 0}
        for i in range(1, len(s)):
            if s[i] in seen_characters:
                dp[i] = sum(dp[: i]) - sum(dp[:seen_characters[s[i]]])
            else:
                dp[i] = 1 + sum(dp[: i])
            seen_characters[s[i]] = i
        print(dp)
        return sum(dp) % MOD



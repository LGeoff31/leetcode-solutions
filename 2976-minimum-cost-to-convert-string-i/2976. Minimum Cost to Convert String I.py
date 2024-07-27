class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dp = [[1e9] * 26 for _ in range(26)]
        print(ord("a") - 97)
        for i in range(len(original)):
            dp[ord(original[i]) - 97 ][ord(changed[i])  - 97] = min(dp[ord(original[i]) - 97 ][ord(changed[i])  - 97], cost[i])
        for i in range(len(dp)):
            dp[i][i] = 0
        
        # Apply Floyds Warshal
        for k in range(len(dp)):
            for i in range(len(dp)):
                for j in range(len(dp)):
                    if dp[i][k] < 1e9 and dp[k][j] < 1e9:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        res = 0
        print(dp)
        for i in range(len(source)):
            num = dp[ord(source[i])  - 97][ord(target[i])  - 97]
            if num == 1e9: return -1
            res += num
        return res



        
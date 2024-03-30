class Solution:
    def minimumSubarrayLength(self, A: List[int], target: int) -> int:
        N = len(A)

        ans = N + 1
        dp = {}
        for j, y in enumerate(A):
            dp = {y | x : i for x, i in dp.items()}
            dp[y] = max(dp.get(y, j), j)
            
            for x, i in dp.items():
                if x >= target:
                    ans = min(ans, j - i + 1)
        
        return ans if ans <= N else -1
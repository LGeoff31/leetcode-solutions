class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        #dp[i][j] = longest subsequence ending index i with at most j changes
        dp = [[1] * (k+1) for _ in range(n)]
        for i in range(n): #O(N)
            for j in range(k+1): #O(K)
                for l in range(i): #everything before i #O(N)
                    if nums[i] == nums[l]: 
                        dp[i][j] = max(1 + dp[l][j], dp[i][j]) 
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[l][j-1] + 1)
        return max(max(row) for row in dp)
        
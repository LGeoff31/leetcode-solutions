class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        """
        Definitely a DP type of problem
        As soon as we find one palindromic word, we can do 1 + dfs(remainder)
        Insight, as soon as we build out a palindromic word of size k, we should go next
        """

        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        for end in range(n):
            for start in range(end, -1, -1):
                if s[start] == s[end] and (end - start < 2 or is_pal[start+1][end-1]):
                    is_pal[start][end] = True 
            
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):         
            for start in range(i + 1):         
                res = dp[i+1][start]                        
                res = max(res, dp[i+1][i])                   
                length = i - start + 1
                if length >= k and is_pal[start][i]:
                    res = max(res, 1 + dp[i+1][i+1])        
                dp[i][start] = res

        return dp[0][0]
        # @cache
        # def dfs(i, start): # O(N * N)
        #     if i == n:
        #         return 0

        #     res = dfs(i+1, start) # skip
        #     res = max(res, dfs(i+1, i)) # take
        #     length = i - start + 1

        #     if length >= k and is_pal[start][i]:
        #         res = max(res, 1 + dfs(i+1, i+1))
        #     return res

        # res = int(dfs(0, 0))
        # dfs.cache_clear()
        # return res
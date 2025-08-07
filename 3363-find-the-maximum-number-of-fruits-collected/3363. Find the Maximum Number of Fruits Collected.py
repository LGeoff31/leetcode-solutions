class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        res = 0
        n = len(fruits)
        for i in range(n):
            res += fruits[i][i]
            fruits[i][i] = 0
        # dp = [[0] * n for _ in range(n)]
        @cache
        def dfs(r,c,bottomleft):
            if not (0 <= r < n and 0 <= c < n):
                return -1e9
            if r == n-1 and c == n-1:
                return fruits[r][c]
            
            if bottomleft and c >= ceil(n/2) and r < floor(n/2):
                return -1e9
            if not bottomleft and c < floor(n/2) and r >= ceil(n/2):
                return -1e9
            
            if bottomleft:
                return fruits[r][c] + max(dfs(r-1,c+1,bottomleft), dfs(r,c+1,bottomleft), dfs(r+1,c+1,bottomleft))
            else:
                return fruits[r][c] + max(dfs(r+1,c-1,bottomleft), dfs(r+1,c,bottomleft), dfs(r+1,c+1,bottomleft))

        return res + dfs(0, n-1, False) + dfs(n-1, 0, True)
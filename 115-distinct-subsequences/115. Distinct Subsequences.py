class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i,j):
            if j == len(t): return 1
            elif i == len(s): return 0
            elif (i,j) in memo:
                return memo[(i,j)]
            elif s[i] == t[j]:
                memo[(i+1, j+1)] = dfs(i+1, j+1)
                memo[(i+1, j)] = dfs(i+1, j)
                return memo[(i+1, j+1)] + memo[(i+1, j)]
            else:
                memo[(i+1, j)] = dfs(i+1, j)
                return memo[(i+1, j)]

        return dfs(0,0)
        
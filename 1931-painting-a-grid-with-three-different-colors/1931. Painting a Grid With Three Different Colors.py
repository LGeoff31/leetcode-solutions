class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        rows, cols = m, n
        cache = {}
        def dfs(prevCol, col, prevUp, r, c): # [0, 1, 0, 2] up length R
            if (tuple(prevCol), tuple(col), prevUp, r, c) in cache:
                return cache[(tuple(prevCol), tuple(col), prevUp, r, c)]
            if r == rows:
                return dfs(col, [], -1, 0, c+1)
            if c == cols:
                return 1

            total = 0 
            for i in range(3):
                if i != prevUp and i != prevCol[r]:
                    total += dfs(prevCol, col + [i], i, r+1, c)
            cache[(tuple(prevCol), tuple(col), prevUp, r, c)] = total % MOD
            return total % MOD
        
        return dfs([-1] * rows, [], -1, 0, 0) % MOD

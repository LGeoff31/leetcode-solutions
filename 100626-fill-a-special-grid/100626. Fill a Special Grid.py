class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        rows, cols = 2**N, 2**N
        res = [[0] * cols for _ in range(rows)]
        maxValue = -1
        # The value in cells should go from 0 -> rows*cols-1
        def dfs(l, r, b, t):
            nonlocal maxValue
            if l > r or t > b:
                return
            if l == r and b == t:
                res[t][l] = maxValue + 1
                maxValue += 1
                return
            mid_col = (l + r) // 2
            mid_row = (b + t) // 2
            
            # Top right
            dfs(mid_col + 1, r, mid_row, t)
            # Bottom right
            dfs(mid_col + 1, r, b, mid_row + 1)
            # Bottom left
            dfs(l, mid_col, b, mid_row + 1)
            # Top left
            dfs(l, mid_col, mid_row, t)
            
        dfs(0, cols-1, rows-1, 0)
        return res
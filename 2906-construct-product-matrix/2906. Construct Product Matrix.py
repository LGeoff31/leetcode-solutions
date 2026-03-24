class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        lst = []
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                lst.append(grid[r][c])
        
        prefix = [1] * (rows * cols)
        prefix[0] = lst[0]
        for i in range(1, rows * cols):
            prefix[i] = (prefix[i-1] * lst[i]) % MOD
        
        suffix = [1] * (rows * cols)
        suffix[-1] = lst[-1]

        for i in range(rows * cols - 2, -1, -1):
            suffix[i] = (suffix[i+1] * lst[i]) % MOD
        
        for i in range(rows * cols):
            r_value = i // cols
            c_value = i % cols

            if i == 0: # start
                val = suffix[1]
            elif i == rows * cols - 1: # end
                val = prefix[-2]
            else:
                val = prefix[i-1] * suffix[i+1]
            grid[r_value][c_value] = val % MOD
        return grid

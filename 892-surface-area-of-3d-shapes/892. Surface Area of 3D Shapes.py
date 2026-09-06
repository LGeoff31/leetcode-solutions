class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        """
        bottom: 4 = 4
        sides: 2 + 4 + 6 + 8 = 20 
        top: 4
        inner sides: 1 + 3 + 2 = 6

        9 + 9 - 2 + 
        """
        res = 0
        # BOTTOM
        n = len(grid)
        if n==1:
            if grid[0][0] == 0:
                return 0
            return 2 + 4 * (grid[0][0])
        for r in range(n):
            for c in range(n):
                if grid[r][c] != 0:
                    res += 1
        # TOP
        res *= 2
        print(res)
        # OUTSIDE SIDES 
        for r in range(n):
            for c in range(n):
                if (r == 0 and c == 0) or (r == 0 and c == n-1) or (c == 0 and r == n-1) or (r == n-1 and c == n-1):
                    res += 2 * grid[r][c]
                elif r == 0 or c == 0 or r == n-1 or c == n-1:
                    res += grid[r][c]
        print(res)
        # INNER SIDES
        for r in range(n):
            for c in range(n):
                if r-1 >= 0:
                    res += max(grid[r][c] - grid[r-1][c], 0)
                if r+1 < n:
                    res += max(grid[r][c] - grid[r+1][c], 0)
                if c-1 >= 0:
                    res += max(grid[r][c] - grid[r][c-1], 0)
                if c+1 < n:
                    res += max(grid[r][c] - grid[r][c+1], 0)
        return res  
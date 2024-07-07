class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[(0,0)] * cols for _ in range(rows)]
        # print(dp)
        # First row
        x_count, y_count = 0, 0
        for c in range(cols):
            if grid[0][c] == "X": x_count += 1
            if grid[0][c] == "Y": y_count += 1
            dp[0][c] = (x_count, y_count)

        x_count, y_count = 0, 0
        # First column
        for r in range(rows):
            if grid[r][0] == "X": x_count += 1
            if grid[r][0] == 'Y': y_count += 1
            dp[r][0] = (x_count, y_count)
        # print("Dp", dp)
        for r in range(1, rows):
            for c in range(1, cols):
                add_x = grid[r][c] == "X"
                add_y = grid[r][c] == "Y"
                if add_x:
                    dp[r][c] = (dp[r][c-1][0] + dp[r-1][c][0] - dp[r-1][c-1][0] + 1, dp[r][c-1][1] + dp[r-1][c][1] - dp[r-1][c-1][1])
                elif add_y:
                    dp[r][c] = (dp[r][c-1][0] + dp[r-1][c][0] - dp[r-1][c-1][0], dp[r][c-1][1] + dp[r-1][c][1] - dp[r-1][c-1][1] + 1)
                else:
                    dp[r][c] = (dp[r][c-1][0] + dp[r-1][c][0] - dp[r-1][c-1][0], dp[r][c-1][1] + dp[r-1][c][1] - dp[r-1][c-1][1])

        # print("next dp", dp)
        # FId msot top left X
        x_vert, x_horz = 1e9, 1e9
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "X":
                    x_vert = min(x_vert, r)
                    x_horz = min(x_horz, c)
        s = [[0] * cols for _ in range(rows)]
        s[0][0] = 1 if grid[0][0] == "X" else 0
        for r in range(1, rows):
            if grid[r][0] == "X":
                s[r][0] = 1 + s[r-1][0]
            else:
                s[r][0] = s[r-1][0]
        for c in range(1, cols):
            if grid[0][c] == "X":
                s[0][c] = 1 + s[0][c-1]
            else:
                s[0][c] = s[0][c-1]
        for r in range(1, rows):
            for c in range(1, cols):
                s[r][c] = s[r-1][c] + s[r][c-1]
                if grid[r][c] == "X":
                    s[r][c] += 1
        # print("S", s)
        res = 0
        for r in range(rows):
            for c in range(cols):
                if dp[r][c][0] == dp[r][c][1] and s[r][c]:
                    print(r,c, x_vert, x_horz)
                    res += 1
        return res

        
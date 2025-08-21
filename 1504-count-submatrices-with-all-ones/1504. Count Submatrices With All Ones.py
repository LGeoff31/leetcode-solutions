class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        rows, cols = len(mat), len(mat[0])
        grid = [[[0,0] for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    continue
                new_x, new_y = 1, 1
                if r > 0:
                    new_y += grid[r-1][c][1]
                if c > 0:
                    new_x += grid[r][c-1][0]
                grid[r][c] = [new_x, new_y]
                min_width = new_x
                rr = r
                while rr >= 0 and mat[rr][c] == 1:
                    if grid[rr][c][0] < min_width:
                        min_width = grid[rr][c][0]
                    res += min_width
                    rr -= 1

        return res
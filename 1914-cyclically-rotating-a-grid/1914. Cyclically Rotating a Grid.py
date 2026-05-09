class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        l, r, t, b = 0, cols - 1, 0, rows - 1

        for _ in range(min(rows, cols) // 2):
            p = 2 * (b-t+1) + 2 * (r-l+1) - 4
            for _ in range(k%p):
                tmp = grid[t][l]
                j = l
                while j < r:
                    grid[t][j] = grid[t][j+1]
                    j += 1
                j = t
                while j < b:
                    grid[j][r] = grid[j+1][r]
                    j += 1
                j = r
                while j > l:
                    grid[b][j] = grid[b][j-1]
                    j -= 1
                j = b
                while j > t:
                    grid[j][l] = grid[j-1][l]
                    j -= 1
                grid[t+1][l] = tmp
            l += 1
            r -= 1
            t += 1
            b -= 1
        return grid





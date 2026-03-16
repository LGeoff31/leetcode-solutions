class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        s = set()

        for i in range(m):
            for j in range(n):
                s.add(grid[i][j])

                k = 1
                while True:
                    if i-k<0 or i+k>=m or j-k<0 or j+k>=n:
                        break

                    total = 0

                    r, c = i-k, j
                    for t in range(k):
                        total += grid[r+t][c+t]

                    r, c = i, j+k
                    for t in range(k):
                        total += grid[r+t][c-t]

                    r, c = i+k, j
                    for t in range(k):
                        total += grid[r-t][c-t]

                    r, c = i, j-k
                    for t in range(k):
                        total += grid[r-t][c+t]

                    s.add(total)
                    k += 1

        return sorted(s, reverse=True)[:3]
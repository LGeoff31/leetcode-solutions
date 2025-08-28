class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            a = []
            new_c = 0
            for new_r in range(r, rows):
                a.append(grid[new_r][new_c])
                new_c += 1
            a.sort(reverse=True)
            i = 0
            new_c = 0
            for new_r in range(r, rows):
                grid[new_r][new_c] = a[i]
                new_c += 1
                i += 1
        for c in range(1, cols):
            a = []
            new_r = 0
            for new_c in range(c, cols):
                a.append(grid[new_r][new_c])
                new_r += 1
            a.sort()
            i = 0
            new_r = 0
            for new_c in range(c, cols):
                grid[new_r][new_c] = a[i]
                new_r += 1
                i += 1
            

        return grid


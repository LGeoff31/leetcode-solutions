class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def pal(arr):
            l, r = 0, len(arr) - 1
            count = 0
            while l <= r:
                if arr[l] != arr[r]:
                    count += 1
                l += 1
                r -= 1
            return count
        res = 1e9
        a = 0
        # Rows
        for arr in grid:
            a += pal(arr)
        b = 0
        # cols
        for c in range(cols):
            z=[]
            for r in range(rows):
                z.append(grid[r][c])
            b += pal(z)

        res = min(res, a, b)
        return res
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        numberDiagonals = 2*n-1
        for i in range(n-1, -1, -1):
            r,c = i, 0
            arr = []
            while r < n and c < n:
                arr.append(grid[r][c])
                r += 1
                c += 1
            arr.sort(reverse=True)
            print(arr)
            idx = 0
            r,c = i, 0
            while r < n and c < n:
                grid[r][c] = arr[idx]
                r += 1
                c += 1
                idx += 1
        for i in range(1, n):
            r,c = 0, i
            arr = []
            while r < n and c < n:
                arr.append(grid[r][c])
                r += 1
                c += 1
            arr.sort()
            idx = 0
            r,c = 0, i
            while r < n and c < n:
                grid[r][c] = arr[idx]
                r += 1
                c += 1
                idx += 1
        print(grid)
        return grid
            
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # If a number is <= 10, it can't be contained in a magic square
        rows, cols = len(grid), len(grid[0])

        def is_magic_square(arr):
            sums = []
            unique_nums = set()
            for row in arr:
                sums.append(sum(row))
            for c in range(3):
                col_sum = 0
                for r in range(3):
                    col_sum += arr[r][c]
                    unique_nums.add(arr[r][c])
                    if arr[r][c] >= 10 or arr[r][c] == 0:
                        return False
                sums.append(col_sum)
            sums.append(arr[0][0] + arr[1][1] + arr[2][2])
            sums.append(arr[-1][0] + arr[1][1] + arr[0][2])
            sums.sort()
            print(sums, arr)
            return sums[0] == sums[-1] and len(unique_nums) == 9

        res = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic_square([[grid[r][c], grid[r][c+1], grid[r][c+2]], [grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2]], [grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]]]):
                    res += 1
        return res
                
        
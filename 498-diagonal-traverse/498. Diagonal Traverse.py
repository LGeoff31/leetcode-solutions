class Solution:
    def findDiagonalOrder(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        # (0,0)
        # (0,1), (1,0)
        # (0, 2), (1,1), (2, 0)
        # (0, 3), (1,2), (2,1), (3,0)
        res = []
        up = True
        maxSum = rows - 1 + cols - 1
        curr = 0
        print(maxSum)
        while True:
            if up:
                # Start maximum row
                    
                r, c = curr, 0
                if curr > rows - 1:
                    r = rows -1 # 4 - 2-1 = 1
                    c = curr - rows + 1
                while 0 <= r < rows and 0 <= c < cols:
                    res.append(grid[r][c])
                    r -= 1
                    c += 1
            else:
                r,c = 0, curr
                if curr > cols - 1:
                    c = cols -1
                    r = curr - cols + 1
                while 0 <= r < rows and 0 <= c < cols:
                    res.append(grid[r][c])
                    r += 1
                    c -= 1
            up = not up
            # print(res, curr)
            curr += 1
            if curr == maxSum + 1:
                break
        return res


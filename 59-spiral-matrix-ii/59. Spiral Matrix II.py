class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n-1
        top, bottom = 0, n-1
        res = [[-1] * n for _ in range(n)]
        cnt = 1
        if n == 1: return [[1]]
        while True:
            # left to right
            for l in range(left, right + 1):
                res[top][l] = cnt
                cnt += 1
            print(cnt)
            # right to bottom
            for r in range(top + 1, bottom + 1):
                res[r][right] = cnt
                cnt += 1
            print(cnt)
            # right to left
            for l in range(right-1, left-1, -1):
                res[bottom][l] = cnt
                cnt += 1
            print(cnt)
            # bottom to up
            for r in range(bottom - 1, top, -1):
                res[r][left] = cnt
                cnt += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
            print('reached', left, right, bottom, top, cnt)
            if cnt == n*n+1:
                break
        return res
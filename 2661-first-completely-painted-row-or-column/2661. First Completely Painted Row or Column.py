class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        if rows == 1 or cols == 1: return 0
        dic = {} # Map num -> (r,c)
        for r in range(rows):
            for c in range(cols):
                dic[mat[r][c]] = (r,c)
        def valid(idx):
            if idx == rows * cols: return True
            grid = [[0] * cols for _ in range(rows)]
            for i in range(idx + 1):
                r,c = dic[arr[i]]
                grid[r][c] = 1
            # print(grid)
            print()
            # Check all rows
            for r in range(rows):
                v = True
                for c in range(cols):
                    if grid[r][c] == 0: v = False
                if v: return True
            # Check all cols
            for c in range(cols):
                v = True
                for r in range(rows):
                    if grid[r][c] == 0: v = False
                if v: return True
            return False
        res = 1e9

        l, r = 0, len(arr) - 1
        print(l, r)
        while l <= r:
            mid = (l + r) // 2
            print('trying', mid, valid(mid), valid(mid+1))
            if not valid(mid) and  valid(mid+1):
                res = min(res, mid + 1)
                r = mid - 1
            elif valid(mid) and valid(mid+1):
                r = mid - 1
            else:
                l = mid + 1
        return res
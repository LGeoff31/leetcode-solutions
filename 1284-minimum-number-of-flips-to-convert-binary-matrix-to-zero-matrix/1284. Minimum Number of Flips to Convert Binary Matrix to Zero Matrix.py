class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        # Flipping same index twice deos nothing
        rows, cols = len(mat), len(mat[0])
        lst = []
        def dfs(idx, arr):
            if idx == rows*cols:
                lst.append(arr)
                return
            dfs(idx+1, arr + [0])
            dfs(idx+1, arr + [1])
        dfs(0, [])
        res = 1e9
        for arr in lst:
            mat_copy = deepcopy(mat)
            for i in range(len(arr)):
                if arr[i] == 1:
                    r,c = i // cols, i % cols
                    mat_copy[r][c] = not mat_copy[r][c]
                    # up
                    if r-1 >= 0: mat_copy[r-1][c] = not mat_copy[r-1][c]
                    # down
                    if r+1 < rows: mat_copy[r+1][c] = not mat_copy[r+1][c]
                    # left
                    if c-1 >= 0: mat_copy[r][c-1] = not mat_copy[r][c-1]
                    # right
                    if c+1 < cols: mat_copy[r][c+1] = not mat_copy[r][c+1]
            print(arr, mat_copy)
            valid = True
            for i in range(len(mat_copy)):
                for j in range(len(mat_copy[i])):
                    if mat_copy[i][j] == 1:
                        valid = False 
            if valid: 
                res = min(res, arr.count(1))

        return res if res != 1e9 else -1

        print(lst)
        print(len(lst))
        return
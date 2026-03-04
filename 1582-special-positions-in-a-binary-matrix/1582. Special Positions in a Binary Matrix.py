class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        def isValid(r,c):
            for dc in range(cols):
                if mat[r][dc] == 1 and dc != c:
                    return False 
            for dr in range(rows):
                if mat[dr][c] == 1 and r != dr:
                    return False 
            return True 
        res = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    res += isValid(r,c)
        return res
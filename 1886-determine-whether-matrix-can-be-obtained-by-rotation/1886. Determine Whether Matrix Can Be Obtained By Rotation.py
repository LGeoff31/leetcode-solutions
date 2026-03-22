class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """

        0 0 1 0
        0 1 1 0
        1 1 1 1
        0 0 1 1

        """
        rows, cols = len(mat), len(mat[0])
        def rotation(mat):
            # returns the rotation matrix
            new_copy = deepcopy(mat)
            for r in range(rows // 2):
                # left -> top
                for c in range(cols - 2*r - 1):
                    mat[r][r + c] = new_copy[rows - c - r - 1][r]
                # top -> right
                for c in range(cols - 2*r):
                    mat[r + c][cols - 1 - r] = new_copy[r][c + r]
                # right -> bottom
                for c in range(cols - 2*r):
                    mat[rows - r - 1][cols - c - r - 1] = new_copy[r + c][cols - r - 1]
                # bottom -> left
                for c in range(cols - 2*r):
                    mat[rows - r - c - 1][r] = new_copy[rows - r - 1][cols - c - r - 1]
            return mat
        if mat == target:
            return True
        for i in range(3):
            mat = rotation(mat)
            if mat == target:
                return True 
        return False


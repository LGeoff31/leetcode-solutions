class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        prefixMat = []
        for r in range(rows):
            prefixRow = []
            for c in range(cols):
                if not prefixRow:
                    prefixRow.append(mat[r][c])
                else:
                    prefixRow.append(mat[r][c] + prefixRow[-1])
            prefixMat.append(prefixRow)
        print(prefixMat)

        l,r = 1, min(rows, cols)

        def valid_square(length):
            for r in range(rows):
                for c in range(cols):
                    # Start a square with sidelength = length starting topleft (r, c)
                    if not (0 <= r + length - 1< rows and 0 <= c + length - 1 < cols):
                        continue
                    square_sum = 0
                    for d1 in range(length):
                        if c==0:
                            square_sum += prefixMat[r+d1][c+length-1]
                        else:
                            square_sum += prefixMat[r+d1][c+length-1] - prefixMat[r+d1][c-1]

                    if square_sum <= threshold:
                        return True
            return False

        while l <= r:
            mid = (l + r) // 2
            print('trying mid', mid, valid_square(mid))
            if valid_square(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return r
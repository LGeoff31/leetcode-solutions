class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        rook_r, rook_c = -1, -1
        res = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "R":
                    rook_r,rook_c = r,c
        print(rook_r, rook_c)
        # going up
        new_r = rook_r-1
        while new_r >= 0:
            if board[new_r][rook_c] == "p":
                res += 1
                break
            elif board[new_r][rook_c] == "B":
                break
            new_r -= 1
        # going down
        new_r = rook_r+1
        while new_r < rows:
            if board[new_r][rook_c] == "p":
                res += 1
                break
            elif board[new_r][rook_c] == "B":
                break
            new_r += 1
         # going left
        new_c = rook_c - 1
        while new_c >= 0:
            if board[rook_r][new_c] == "p":
                res += 1
                break
            elif board[rook_r][new_c] == "B":
                break
            new_c -= 1
        # going right
        new_c = rook_c + 1
        while new_c < cols:
            if board[rook_r][new_c] == "p":
                res += 1
                break
            elif board[rook_r][new_c] == "B":
                break
            new_c += 1
        return res
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        res=0
        
        for r in range(rows):
            for c in range(cols):
                valid = True
                if r-1 >= 0:
                    if board[r-1][c] == "X":
                        valid = False 
                if c-1 >= 0:
                    if board[r][c-1] == "X":
                        valid = False 
                res += valid and board[r][c] == "X"
        return res
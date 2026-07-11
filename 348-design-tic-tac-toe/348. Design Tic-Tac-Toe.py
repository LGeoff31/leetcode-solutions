class TicTacToe:
    """
    0 -> none
    1 -> player 1
    2 -> player 2

    0 2
    1 2

    """
    def check_game_status(self, board):
        # DIGONAL CHECKS
        curr = board[0][0]
        DIAGONAL_TOP_LEFT_BOTTOM_RIGHT = True
        for i in range(self.n):
            if board[i][i] != curr or curr == 0:
                DIAGONAL_TOP_LEFT_BOTTOM_RIGHT = False 
        curr = board[-1][0]
        DIAGONAL_TOP_RIGHT_BOTTOM_LEFT = True
        for i in range(self.n):
            if board[i][self.n - i - 1] != curr or curr == 0:
                DIAGONAL_TOP_RIGHT_BOTTOM_LEFT = False

        # HORIZONTAL CHECKS
        HORZONTAL_WIN = False
        for r in range(self.n):
            curr =  board[r][0]
            HORZONTAL_WIN_ROW = True
            for c in range(self.n):
                if curr == 0 or board[r][c] != curr:
                    HORZONTAL_WIN_ROW = False 
            if HORZONTAL_WIN_ROW:
                HORZONTAL_WIN = True 
        
        # VERTICAL CHECKS
        """
        0 2
        1 2
        """
        VERTICAL_WIN = False
        for c in range(self.n):
            curr = board[0][c]
            VERTICAL_WIN_ROW = True
            for r in range(self.n):
                if curr == 0 or board[r][c] != curr:
                    VERTICAL_WIN_ROW = False 
            if VERTICAL_WIN_ROW:
                VERTICAL_WIN = True 

        if DIAGONAL_TOP_LEFT_BOTTOM_RIGHT or DIAGONAL_TOP_RIGHT_BOTTOM_LEFT or HORZONTAL_WIN or VERTICAL_WIN:
            return [True, "win"]
        if all(board[r][c] != 0 for r in range(self.n) for c in range(self.n)):
            return [True, "tie"]
        return [False, "in progress"]

    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n for _ in range(n)] 
        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        status, quote = self.check_game_status(self.board)
        if status:
            if quote == "win":
                return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
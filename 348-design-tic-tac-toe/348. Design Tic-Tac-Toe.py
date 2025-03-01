class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows1 = [0] * self.n
        self.cols1 = [0] * self.n
        self.rows2 = [0] * self.n
        self.cols2 = [0] * self.n
        self.diagonal1_tl_br = 0
        self.diagonal1_tr_bl = 0
        self.diagonal2_tl_br = 0
        self.diagonal2_tr_bl = 0


    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.rows1[row] += 1
            self.cols1[col] += 1
            if row == col:
                self.diagonal1_tl_br += 1
            if row == self.n - col - 1:
                self.diagonal1_tr_bl += 1
            if max(self.rows1[row], self.cols1[col], self.diagonal1_tl_br, self.diagonal1_tr_bl) == self.n:
                return 1
        else:
            self.rows2[row] += 1
            self.cols2[col] += 1
            if row == col:
                self.diagonal2_tl_br += 1
            if row == self.n - col - 1:
                self.diagonal2_tr_bl += 1
            if max(self.rows2[row], self.cols2[col], self.diagonal2_tl_br, self.diagonal2_tr_bl) == self.n:
                return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
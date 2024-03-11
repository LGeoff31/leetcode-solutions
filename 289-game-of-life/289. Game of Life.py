class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        newBoard = [[0] * len(board[0]) for _ in range(len(board))]
        print(newBoard)
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                directions = (-1, 0, 1)
                aliveCount = 0
                for x in directions:
                    for y in directions:
                        if 0<=r+x<rows and 0<=c+y<cols and not (x==0 and y == 0) and board[r+x][c+y] == 1:
                            aliveCount += 1
                if board[r][c] == 1:
                    if aliveCount == 2 or aliveCount == 3: newBoard[r][c] = 1
                    else: newBoard[r][c]=0
                else:
                    if aliveCount == 3: newBoard[r][c] = 1
        for i in range(len(newBoard)):
            for j in range(len(newBoard[0])):
                board[i][j] = newBoard[i][j]
        
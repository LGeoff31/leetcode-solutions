class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        def dfs(r,c):
            if not (0 <= r < rows and 0 <= c < cols): 
                return
            if board[r][c] == "M":
                board[r][c] = "X"
                return
            if board[r][c] == "E":
                # Check if should replace with 1-8
                bombsAround = 0
                for r2, c2 in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r,c), (r,c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
                    if 0 <= r2 < rows and 0 <= c2 < cols:
                        bombsAround += board[r2][c2] == "M"
                if bombsAround == 0:
                    board[r][c] = "B"
                    for r2, c2 in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r,c), (r,c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
                        if 0<=r2<rows and 0<=c2<cols and board[r2][c2] == "E": dfs(r2, c2)
                else:
                    board[r][c] = str(bombsAround)
            # print(board)
        # Mutate the board
        dfs(click[0], click[1])
        return board
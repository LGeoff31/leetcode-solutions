class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #1.) Array contain all elements in 3x3 cubes
        #2.) Array contain all elements in row
        #3.) Array contain all elements in column
        n = 9
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)
        currFilledIn = 0
        for r in range(n):
            for c in range(n):
                elem = board[r][c]
                if elem != ".":
                    currFilledIn+=1
                    rows[r].append(elem)
                    cols[c].append(elem)
                    squares[3 * (c//3) + r//3].append(elem)
        
        def dfs(board, currFilledIn):
            # print('currFilled', currFilledIn)
            if currFilledIn == 81:
                return True

            for r in range(n):
                for c in range(n):
                    if board[r][c] == ".":
                        for num in range(1, 10):
                            num = str(num)
                            if num not in rows[r] and num not in cols[c] and num not in squares[3 * (c//3) + r//3]:
                                rows[r].append(num)
                                cols[c].append(num)
                                squares[3 * (c//3) + r//3].append(num)
                                board[r][c] = num

                                if dfs(board, currFilledIn+1): return True

                                board[r][c] = "."
                                rows[r].remove(num)
                                cols[c].remove(num)
                                squares[3 * (c//3) + r//3].remove(num)
                        return False



        print(dfs(board, currFilledIn))
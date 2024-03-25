class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        queue = deque([board])
        visited = set()
        visited.add((board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2]))
        # print(visited)
        # return False
        def checkWin(board):
            if board[0][0] == 1 and board[0][1] == 2 and board[0][2] == 3 and board[1][0] == 4 and board[1][1] == 5 and board[1][2] == 0: return True
            return False
        if checkWin(board): return 0
        
        def checkVisited(board):
            if (board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2]) in visited: return True
            return False
        count=1
        while queue:
            for i in range(len(queue)):
                brd = queue.popleft()
                zeroIdx = (-1, -1)

                if brd[0][0] == 0: zeroIdx=(0,0)
                elif brd[0][1] == 0: zeroIdx=(0,1)
                elif brd[0][2] == 0: zeroIdx=(0,2)
                elif brd[1][0] == 0: zeroIdx=(1,0)
                elif brd[1][1] == 0: zeroIdx=(1,1)
                elif brd[1][2] == 0: zeroIdx=(1,2)

                r,c = zeroIdx
                #check up
                if r-1 == 0:
                    a=copy.deepcopy(brd)
                    a[r][c], a[r-1][c] = a[r-1][c], a[r][c]
                    if checkWin(a): return count
                    if not checkVisited(a): 
                        visited.add((a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2]))
                        queue.append(a)
                #check right
                if c+1 <= 2:
                    a=copy.deepcopy(brd)
                    a[r][c], a[r][c+1] = a[r][c+1], a[r][c]
                    if checkWin(a): return count
                    if not checkVisited(a): 
                        visited.add((a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2]))
                        queue.append(a)
                #check left
                if c-1 >= 0:
                    a=copy.deepcopy(brd)
                    a[r][c], a[r][c-1] = a[r][c-1], a[r][c]
                    if checkWin(a): return count
                    if not checkVisited(a): 
                        visited.add((a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2]))
                        queue.append(a)
                #check down
                if r+1==1:
                    a=copy.deepcopy(brd)
                    a[r][c], a[r+1][c] = a[r+1][c], a[r][c]
                    if checkWin(a): return count
                    if not checkVisited(a): 
                        visited.add((a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2]))
                        queue.append(a)
            count+=1
        return -1

        
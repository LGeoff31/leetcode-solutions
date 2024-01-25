class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word, visited):
            #base case
            # print("word", word)
            if len(word) == 0:
                return True
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for di, dj in directions:
                ni, nj = i + di, j+dj
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == word[0] and (ni,nj) not in visited:
                    new_visited = set(visited)
                    new_visited.add((ni,nj))
                    if dfs(ni, nj, word[1:], new_visited):
                        return True
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:], {(i,j)}):
                        return True
        return False
        
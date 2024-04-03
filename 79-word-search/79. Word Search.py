
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 1 and len(board[0]) == 1 and len(word) == 1 and word[0] == board[0][0]: return True
        def dfs(r, c, idx, visited):
            if idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols: return False
            if (r,c) in visited: return False
            if board[r][c] != word[idx]: return False
            a = visited.copy()
            a.add((r,c))
            directions = [(-1, 0), (1,0), (0, 1), (0, -1)]
            for dr, dc in directions:
                if 0 <= r + dr < rows and 0 <= c + dc < cols:
                    if dfs(r+dr, c+dc, idx+1, a): 
                        return True

            return False
            
        
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c, 0, set()):
                        return True
        return False
       

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows, cols = len(board), len(board[0])
        def dfs(r,c, idx, visited):
            if idx == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols) or (r,c) in visited:
                return False
            visited.add((r,c))
            res = False
            if board[r][c] == word[idx]:
                res = dfs(r-1, c, idx + 1, visited) or dfs(r+1, c, idx + 1, visited) or dfs(r, c-1, idx + 1, visited) or dfs(r, c+1, idx + 1, visited)
            visited.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, 0, set()):
                    return True
        return False

        # a b c e
        # s f e s
        # a d e e
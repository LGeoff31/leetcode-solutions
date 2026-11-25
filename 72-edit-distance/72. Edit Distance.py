class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            
            if i >= len(word1) or j >= len(word2):
                return max(len(word1) - i, len(word2) - j)
            
            moves = float('inf')
            # INSERT
            moves = min(moves, 1 + dfs(i, j+1))

            # DELETE
            moves = min(moves, 1 + dfs(i+1, j))

            # REPLACE
            moves = min(moves, 1 + dfs(i+1, j+1))

            if word1[i] == word2[j]:
                moves = min(moves, dfs(i+1, j+1))
            
            return moves
        
        return dfs(0, 0)
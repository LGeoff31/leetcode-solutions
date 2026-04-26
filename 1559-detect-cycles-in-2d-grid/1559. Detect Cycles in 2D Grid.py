class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        c a d
        a a a
        a a d
        a c d
        a b c

        """
        seen = set()

        def dfs(r,c, prev_r, prev_c, s):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            for new_r, new_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if (new_r == prev_r and new_c == prev_c) or not (0 <= new_r < rows and 0 <= new_c < cols):
                    continue
                if (new_r, new_c) in s:
                    return True
                if grid[r][c] == grid[new_r][new_c]:
                    s.add((new_r, new_c))
                    seen.add((new_r, new_c))
                    if dfs(new_r, new_c, r, c, s):
                        return True
            
            return False
        
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                # print(r,c, seen)
                if (r,c) not in seen:
                    if dfs(r,c, -1, -1, {(r,c)}):
                        return True
        return False
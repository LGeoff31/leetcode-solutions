class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        p, a = set(), set()
        def dfs(r,c,visited):
            if not (0 <= r < rows and 0 <= c < cols) or (r,c) in visited:
                return
            visited.add((r,c))
            for nei_r, nei_c in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                if 0 <= nei_r < rows and 0 <= nei_c < cols and (nei_r, nei_c) not in visited and heights[nei_r][nei_c] >= heights[r][c]:
                    dfs(nei_r, nei_c, visited)
        
        for r in range(rows):
            dfs(r,0,p)
        for c in range(cols):
            dfs(0,c,p)
        
        for r in range(rows):
            dfs(r,cols-1,a)
        for c in range(cols):
            dfs(rows-1,c,a)
        print(list(p&a))
        return list(p & a)
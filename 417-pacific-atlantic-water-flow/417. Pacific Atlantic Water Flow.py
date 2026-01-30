class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []

        def valid(r,c):
            queue = deque([(r,c)])
            visited = set()
            _dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            pac_found = atl_found = False
            print(queue)
            while queue:
                r,c = queue.popleft()
                curr_height = heights[r][c]
                if r == 0 or c == 0:
                    pac_found = True
                if r == rows -1 or c == cols - 1:
                    atl_found = True

                for dr, dc in _dir:
                    new_r, new_c = r+dr, c+dc
                    if 0<=new_r<rows and 0<=new_c<cols and heights[new_r][new_c] <= curr_height and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
            return pac_found and atl_found

        for r in range(rows):
            for c in range(cols):
                if valid(r,c):
                    res.append((r,c))
        return res
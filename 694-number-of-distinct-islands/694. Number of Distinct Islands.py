class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        groups = []
        def bfs(r,c):
            lst = []
            queue = deque([(r,c)])
            visited.add((r,c))
            while queue:
                r,c = queue.popleft()
                lst.append([r,c])
                for new_r, new_c in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and grid[new_r][new_c] == 1:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
            groups.append(lst)
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    visited.add((r,c))
                    bfs(r,c) # This will mutate groups

        # Normalize all groups
        print(groups)
        for arr in groups:
            # Find the rightmost, then topmost
            x,y = sorted(arr, key=lambda x: (-x[1], -x[0]))[0]
            print(x,y)
            # print(x,y)
            for i in range(len(arr)):
                # print(arr[i])
                arr[i][0] -= x
                arr[i][1] -= y
        seen = set()
        count = 0
        for i in range(len(groups)):
            if i not in seen:
                for j in range(i+1, len(groups)):
                    if groups[i] == groups[j]:
                        seen.add(j)
                count += 1
        return count

class Solution:
    def latestDayToCross(self, rows: int, cols: int, cells: List[List[int]]) -> int:
        l, r = 0, len(cells)
        def possible(day):
            filled_cells = set((c[0],c[1]) for c in cells[:day])
            queue = deque([])
            visited = set()
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for c in range(cols):
                if (1, c+1) not in filled_cells:
                    visited.add((1, c+1))
                    queue.append((1, c+1))
            # print(queue)
            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    # print(new_r, new_c)
                    if not (1 <= new_r <= rows and 1 <= new_c <= cols) or (new_r, new_c) in visited or (new_r, new_c) in filled_cells:
                        continue
                    if new_r == rows:
                        return True
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))
            return False
        while l <= r:
            mid = (l + r) // 2
            if possible(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
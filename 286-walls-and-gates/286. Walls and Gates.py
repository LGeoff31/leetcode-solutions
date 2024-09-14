class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr, dc in directions:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and rooms[r+dr][c+dc] == 2147483647:
                        rooms[r + dr][c + dc] =  1 + rooms[r][c]
                        queue.append((r+dr, c+dc))
        return rooms
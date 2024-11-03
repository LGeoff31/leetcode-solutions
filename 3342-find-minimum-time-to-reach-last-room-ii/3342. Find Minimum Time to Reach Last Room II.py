class Solution:
    def minTimeToReach(self, matrix: List[List[int]]) -> int:

        num_rows = len(matrix)
        num_cols = len(matrix[0])
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        priority_queue = [(0, 0, 0, True)]  # time, row, col, is_day

        while priority_queue:
            time, row, col, is_day = heapq.heappop(priority_queue)
            
            if row == num_rows - 1 and col == num_cols - 1:
                return time
                
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (new_row >= num_rows or new_col >= num_cols or 
                    new_row < 0 or new_col < 0 or visited[new_row][new_col]):
                    continue
                visited[new_row][new_col] = True
                additional_time = 1 if is_day else 2
                heapq.heappush(priority_queue, (max(time + additional_time, matrix[new_row][new_col] + additional_time), new_row, new_col, not is_day))
        return -1
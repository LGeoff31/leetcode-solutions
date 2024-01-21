from collections import deque
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_sum = 1e9
        #case matrix empty or has only 1 row
        rows = len(matrix)
        columns = len(matrix[0])
        
        def bfs(row, col, curr_value):
            queue = deque([[row, col, curr_value]])
            min_value = 1e9

            while queue:

                for i in range(len(queue)):
                    r, c, curr_value = queue.popleft()
                    # print(r, c)
                    r += 1 
                    if r == rows:
                        min_value = min(min_value, curr_value)
                        for row, col, value in queue:

                            min_value = min(min_value, value)
                    if r < rows and 0 <= c-1 < columns:
                        queue.append([r, c-1, curr_value + matrix[r][c-1]])
                    if r < rows and 0 <= c < columns:
                        queue.append([r, c, curr_value + matrix[r][c]])
                    if r < rows and 0 <= c+1 < columns:
                        queue.append([r, c+1, curr_value + matrix[r][c+1]])
            return min_value
        # return bfs(0, 0, matrix[0][0])
        for i in range(len(matrix[0])):
            possible_sum = bfs(0, i, matrix[0][i])
            min_sum = min(min_sum, possible_sum)

        return min_sum


        
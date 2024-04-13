class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        heights = [[0] * cols for _ in range(rows)]
        #fill top row
        for c in range(cols):
            heights[0][c] = int(matrix[0][c])

        for r in range(1, rows):
            for c in range(cols):
                if int(matrix[r][c]) != 0:
                    heights[r][c] = 1 + heights[r-1][c]
                else:
                    heights[r][c] = 0
        global_res = 0
        for arr in heights:
            local_res = 0
            stack=[]
            start = 0
            for i, h in enumerate(arr):
                start = i
                while stack and stack[-1][1] > h:
                    idx, height = stack.pop()
                    local_res = max(local_res, height * (i - idx))
                    start = idx
                stack.append([start, h])
            for i, h in stack:
                local_res = max(local_res, h * (len(arr) - i))
            global_res = max(global_res, local_res)
        return global_res
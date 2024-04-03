class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            row = matrix[0]
            left, right = 0, len(matrix[0]) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        rows, cols = len(matrix), len(matrix[0])
        #binary search for col and make sure to stop to lower one
        top, bottom = 0, rows - 1
        row_idx = -1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] == target:
                row_idx = mid
                break
            if mid - 1 >= 0 and matrix[mid-1][0] <= target < matrix[mid][0]:
                print('reached')
                row_idx = mid-1
                break
            elif mid - 1 >= 0 and target < matrix[mid-1][0]:
                bottom = mid - 1
            else:
                top = mid + 1

        if row_idx == -1 and matrix[-1][0] <= target <= matrix[-1][-1]:
            row_idx = rows - 1
        elif row_idx == -1:
            return False
            
        #binary search for row
        row = matrix[row_idx]
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        
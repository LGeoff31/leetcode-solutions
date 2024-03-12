class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        res = []
        visited = set()
        while left <= right:
            try:
                for i in range(left, right + 1): #top left - top right
                    if (top, i) not in visited:
                        res.append(matrix[top][i])
                        visited.add((top, i))
                    else:
                        break
                print(res)
                for i in range(top + 1, bottom + 1): #top right - bottom right
                    if (i, right) not in visited:
                        res.append(matrix[i][right])
                        visited.add((i, right))
                    else:
                        break
                print(res)
                if top == bottom:
                    break
                for i in range(right - 1, left-1, -1): #bottom right - bottom left
                    if (bottom, i) not in visited:
                        visited.add((bottom, i))
                        res.append(matrix[bottom][i])
                    else:
                        break

                print(res)
                for i in range(bottom - 1, top, -1): #bottom left - top left
                    if (i, left) not in visited:
                        visited.add((i, left))
                        res.append(matrix[i][left])
                    else:
                        break
                print(res)
            except:
                break
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res


        
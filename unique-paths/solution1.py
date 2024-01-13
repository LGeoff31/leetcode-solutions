from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 and m == 1:
            return 1
        queue = deque([[0, 0]])
        ways = 0
        while queue:
            for i in range(len(queue)):
                leftmost_coordinate = queue.popleft()  # [0,0]
                # check if end position
                if (leftmost_coordinate[0] + 1 == m - 1) and (leftmost_coordinate[1] == n - 1):
                    ways += 1
                elif (leftmost_coordinate[0] == m - 1) and (leftmost_coordinate[1] + 1 == n - 1):
                    ways += 1
                else:
                    # adding x by 1
                    if leftmost_coordinate[0] + 1 <= m - 1:
                        queue.append([leftmost_coordinate[0]+1,
                                     leftmost_coordinate[1]])  # [1,0]
                    # adding y by 1
                    if leftmost_coordinate[1] + 1 <= n - 1:
                        queue.append(
                            [leftmost_coordinate[0], leftmost_coordinate[1]+1])  # [0,1]
            # print(queue)
        return ways

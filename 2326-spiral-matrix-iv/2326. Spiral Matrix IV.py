# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        rows, cols = m, n
        direction = 0 # 0: right, 1: down: 2: left 3: up
        r,c = 0, 0
        loops = 0
        while head:
            res[r][c] = head.val
            if direction == 0:
                c += 1
                if c == cols - loops:
                    c -= 1
                    direction = 1
                    r += 1

            elif direction == 1:
                r += 1
                if r == rows - loops:
                    r -= 1
                    c -= 1
                    direction = 2
            elif direction == 2:
                c -= 1
                if c == -1 + loops:
                    c += 1
                    r -= 1
                    direction = 3
            else:
                r -= 1
                if r == loops:
                    loops += 1
                    r += 1
                    c += 1
                    direction = 0
            head = head.next

        return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None: return []
        queue = deque([root])

        forward = True
        while queue:
            a = []
            for i in range(len(queue)):
                b = queue.popleft()
                a.append(b.val)
                if b.left is not None: queue.append(b.left)
                if b.right is not None: queue.append(b.right)
            if forward: res.append(a)
            else: res.append(a[::-1])
            forward = not forward

        return res
        
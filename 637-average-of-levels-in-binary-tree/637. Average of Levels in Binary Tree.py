# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = [root.val]

        queue = deque([root])

        while queue:
            acc = 0
            length = len(queue)
            for i in range(len(queue)):
                a = queue.popleft()
                acc+=a.val
                if a.left is not None: queue.append(a.left)
                if a.right is not None: queue.append(a.right)
            res.append(acc / length)
        return res[1:]
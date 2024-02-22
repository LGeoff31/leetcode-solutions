# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            queue = deque([root])
        else:
            queue = deque([])
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                root = queue.popleft()
                if root and root.left:
                    queue.append(root.left)
                if root and root.right:
                    queue.append(root.right) 
        return depth

        # if root is None:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        lst = []
        res = [[root.val]]
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    lst.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    lst.append(node.right.val)
                    queue.append(node.right)
            if not lst:
                break
            res.append(lst)
            lst = []
        return res          



        
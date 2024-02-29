# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        if root.val % 2 == 0: return False
        queue = deque([root])
        valid = True
        oddChecker = True

        while queue:
            if oddChecker: #increasing order
                prev = -1
                for i in range(len(queue)):
                    if queue[i].val % 2 == 0 or queue[i].val <= prev:
                        return False
                    prev=queue[i].val
            else: #decreasing order
                prev = 1e9
                for i in range(len(queue)):
                    if queue[i].val % 2 == 1 or queue[i].val >= prev:
                        return False
                    prev = queue[i].val
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)


            oddChecker = not oddChecker
        return True

        
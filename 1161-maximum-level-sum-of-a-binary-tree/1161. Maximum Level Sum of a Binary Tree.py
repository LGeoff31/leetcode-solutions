# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        maxLevel = 1
        level = 1

        queue = deque([root])

        while queue:
            lst = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: 
                    lst.append(node.left.val)
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
                    lst.append(node.right.val)
            level += 1
            print(lst)

            if lst and sum(lst) > maxSum:
                maxSum = sum(lst)
                maxLevel = level

        return maxLevel



        
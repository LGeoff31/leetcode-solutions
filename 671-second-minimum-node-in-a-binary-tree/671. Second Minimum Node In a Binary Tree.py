# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        firstMin = 1e10
        secondMin = 1e10
        def smallest_node(node):
            nonlocal firstMin
            if node:
                firstMin = min(firstMin, node.val)
                smallest_node(node.left)
                smallest_node(node.right)
        def second_smallest_node(node):
            nonlocal secondMin
            if node:
                if node.val != firstMin:
                    secondMin = min(secondMin, node.val)
                second_smallest_node(node.left)
                second_smallest_node(node.right)
        smallest_node(root)
        second_smallest_node(root)

        return secondMin if secondMin != 1e10 else -1
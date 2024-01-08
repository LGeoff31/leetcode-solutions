# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(head, low, high):
            if head is None:
                return 0
            if head.val >= low and head.val <= high:
                return head.val + dfs(head.left, low, high) + dfs(head.right, low, high)
            return dfs(head.left, low, high) + dfs(head.right, low, high)

        return dfs(root, low, high)
        # return result

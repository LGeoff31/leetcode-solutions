# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currSum):
            if node is None: return 0
            currSum += node.val
            if currSum == targetSum: 
                return 1 + dfs(node.left, currSum) + dfs(node.right, currSum)
            else:
                return dfs(node.left, currSum) + dfs(node.right, currSum)
        
        def traversal(node, res):
            if node is None: return 0
            return dfs(node, 0) + traversal(node.left, res) + traversal(node.right, res)

        return traversal(root, 0)

        
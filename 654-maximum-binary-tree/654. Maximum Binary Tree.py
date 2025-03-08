# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if not arr:
                return None
            maxValue = max(arr)
            maxValueIdx = arr.index(maxValue)
            lhs = arr[: maxValueIdx]
            rhs = arr[maxValueIdx+1 : ]
            maxNode = TreeNode(maxValue)
            maxNode.left = dfs(lhs)
            maxNode.right = dfs(rhs)
            return maxNode
        return dfs(nums)
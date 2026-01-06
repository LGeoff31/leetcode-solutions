# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        row_level = 0
        row_summ = -1e9
        cnt = 1
        while queue:
            row_sum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                row_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if row_sum > row_summ:
                row_summ = row_sum
                row_level = cnt
            cnt += 1
        return row_level
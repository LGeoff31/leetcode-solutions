# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        res = 0
        while queue:
            min_val, max_val = 1e9, -1e9
            for i in range(len(queue)):
                node, val = queue.popleft()
                min_val = min(min_val, val)
                max_val = max(max_val, val) 
                if i == 0:
                    min_val = val
                    max_val = val
                if node.left: queue.append((node.left, 2*val))
                if node.right: queue.append((node.right, 2*val+1))
            res = max(res, max_val - min_val + 1)
            print(res)
        return res
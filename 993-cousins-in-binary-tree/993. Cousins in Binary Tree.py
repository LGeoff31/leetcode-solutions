# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        levels = []
        queue = deque([root])
        parent = {}
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    parent[node.left.val] = node.val
                    queue.append(node.left)
                if node.right:
                    parent[node.right.val] = node.val
                    queue.append(node.right)
            levels.append(level)

        for arr in levels:
            if x in arr and y in arr and parent[x] != parent[y]:
                return True
        return False 
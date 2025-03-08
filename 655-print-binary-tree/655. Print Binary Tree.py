# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        r = height(root)
        c = 2**(r) - 1
        print(r,c)
        res = [[""] * c for _ in range(r)]
        queue = deque([(0, (c-1)//2, root)])

        while queue:
            for i in range(len(queue)): # Level by level traversal
                a,b,node = queue.popleft()
                res[a][b] = str(node.val)
                if node.left:
                    queue.append((a+1, b-2**((r-1)-a-1), node.left))
                if node.right:
                    queue.append((a+1, b+2**((r-1)-a-1), node.right))

        return res
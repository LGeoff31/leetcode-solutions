# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def exists(node, num):
            if not node:
                return False
            if node.val == num:
                return True
            elif node.val > num:
                return exists(node.left, num)
            else:
                return exists(node.right, num)
        def double(node, num):
            if not node:
                return False
            if node.val == num:
                if node.left and node.left.val == num or node.right and node.right.val == num:
                    return True
                return False
            elif node.val > num:
                return double(node.left, num)
            else:
                return double(node.right, num)
        def traverse(node):
            if not node:
                return False
            complement = k - node.val
            if exists(root, complement) and complement*2 != k:
                return True
            elif exists(root, complement):
                print('reached', double(root, complement))
                if double(root, complement): return True
                # return double(root, complement)
            return traverse(node.left) or traverse(node.right)
        return traverse(root)
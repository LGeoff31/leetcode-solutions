"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Left, Right, current: Postorder
        self.res = []
        def dfs(node):
            if node:
                for nei in node.children:
                    dfs(nei)
                self.res.append(node.val)
        
        dfs(root)
        return self.res

        
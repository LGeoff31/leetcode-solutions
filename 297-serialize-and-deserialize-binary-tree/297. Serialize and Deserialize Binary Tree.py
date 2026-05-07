# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        def dfs(node):
            if node:
                data.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                data.append("N")
        dfs(root)

        return ",".join(data)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        values = data.split(",")
        def dfs():
            val = values[self.i]
            self.i += 1
            if val == "N":
                return None
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
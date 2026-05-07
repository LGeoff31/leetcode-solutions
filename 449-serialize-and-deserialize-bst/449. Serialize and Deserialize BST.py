# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        data = []
        def dfs(node):
            if node:
                data.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)

        return ",".join(data)


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        def dfs(data):
            if data == "":
                return None
            print(data)
            data = data.split(",")
            val = int(data[0])
            left_index_end = 1
            while left_index_end < len(data):
                if int(data[left_index_end]) >= val:
                    break
                left_index_end += 1

            root = TreeNode(val)
            root.left = dfs(",".join(data[1: left_index_end]))
            root.right = dfs(",".join(data[left_index_end : ]))
            return root

        return dfs(data)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
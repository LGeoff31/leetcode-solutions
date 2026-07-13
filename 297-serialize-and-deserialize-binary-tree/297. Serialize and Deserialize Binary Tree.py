# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
1L2LNRNR3L4R5

PREORDER
CURRENT
LEFT
RIGHT

INORDER
LEFT
CURRENT
RIGHT

POSTORDER
LEFT
RIGHT
CURRENT

"""
class Codec:
    def serialize(self, root):
        if root is None:
            return "#"
        res = ""
        res += str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        return res
        
    def deserialize(self, data):
        lst = data.split(",")
        print(lst)
        def build(idx):
            val = lst[idx]
            idx += 1

            if val == "#":
                return None, idx 
            node = TreeNode(int(val))
            node.left, idx = build(idx)
            node.right, idx = build(idx)
            return node, idx

        root, idx = build(0)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
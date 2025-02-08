# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        # cache = {}
        def valid_children(node_id):
            node = id_to_node[node_id]
            isLeftPath = node.left and abs(node.left.val - node.val) == 1
            isRightPath = node.right and abs(node.right.val - node.val) == 1
            return isLeftPath or isRightPath
        self.res = 1

        @cache
        def dfs(node_id):
            print(node_id)
            node = id_to_node[node_id]
            print('node', node.val)
            # Leaf node
            if node.left == None and node.right == None:
                return (1,1)
            # If none of children satisfy difference of 1 constraint
            if not valid_children(node_id):
                return (1,1)

            largest_decr, largest_incr = 1, 1
            # Finding largest decrement
            if node.left and node.val - node.left.val == 1:
                largest_decr = max(largest_decr, 1 + dfs(id(node.left))[0]) # 1 + 1 + 1
            if node.right and node.val - node.right.val == 1:
                largest_decr = max(largest_decr, 1 + dfs(id(node.right))[0])
            # Find largest increment
            if node.left and node.left.val - node.val == 1:
                largest_incr = max(largest_incr, 1 + dfs(id(node.left))[1])
            if node.right and node.right.val - node.val == 1:
                largest_incr = max(largest_incr, 1 + dfs(id(node.right))[1])
            
            self.res = max(self.res, largest_decr, largest_incr)
            # Combine both
            if node.left and node.right:
                decr_incr, incr_decr = 0, 0
                # Decrement on left, increment on right
                if node.val - node.left.val == 1 and node.right.val - node.val == 1:
                    decr_incr =  1 + dfs(id(node.left))[0] + dfs(id(node.right))[1]
                # Increment on left, decrement on right
                if node.left.val - node.val == 1 and node.val - node.right.val == 1:
                    incr_decr = 1 + dfs(id(node.left))[1] + dfs(id(node.right))[0]
                self.res = max(self.res, decr_incr, incr_decr)

            return (largest_decr, largest_incr)
        id_to_node = {}
        def map_nodes(node):
            if not node:
                return
            id_to_node[id(node)] = node
            map_nodes(node.left)
            map_nodes(node.right)
        map_nodes(root)
        def traversal(node):
            id_to_node[id(node)] = node
            dfs(id(node))
            if node.left: traversal(node.left)
            if node.right: traversal(node.right)
        traversal(root)
        return self.res

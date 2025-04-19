# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # 1. Turn tree into undirected graph
        # 2. BFS from the source node until you get to leaf node (tracked in set)

        dic = defaultdict(list)
        leaf_nodes = set()
        visited = set()
        starting_node = None

        def construct_graph(node, parent):
            nonlocal starting_node 

            if not node:
                return
            if node.val == k:
                starting_node = node
            if node.left is None and node.right is None:
                leaf_nodes.add(node.val)
            if parent != -1:
                dic[node].append(parent)
                dic[parent].append(node)
            construct_graph(node.left, node)
            construct_graph(node.right, node)
        
        visited.add(starting_node)
        construct_graph(root, -1)
        queue = deque([starting_node])
        print(dic[root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.val in leaf_nodes:
                    return node.val
                for nei in dic[node]:
                    # print(nei.val)
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        return None

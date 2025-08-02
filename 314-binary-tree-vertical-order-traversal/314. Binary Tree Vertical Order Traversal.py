from collections import defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        dic = defaultdict(list)

        def dfs(node, row, col):
            if not node:
                return
            dic[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        result = []
        for col in sorted(dic.keys()):
            # sort by row to ensure top-to-bottom
            col_nodes = sorted(dic[col], key=lambda x: x[0])
            result.append([val for _, val in col_nodes])
        
        return result

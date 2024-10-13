# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def valid_power_2(num): #O(logn)
            while num != 1:
                if num%2!=0:
                    return False 
                num//=2
            return True

        def evaluate(node):
            queue = deque([node])
            total_nodes = 0
            height = 0
            while queue:
                if len(queue) != 2**height:
                    return -1
                total_nodes += len(queue)
                for i in range(len(queue)):
                    n = queue.popleft()
                    # Ensure there's not single child
                    if (n.left and not n.right) or (not n.left and n.right):
                        return -1
                    if n.left and n.right:
                        queue.append(n.left)
                        queue.append(n.right)
                height += 1
            return total_nodes

        def dfs(node):
            if not node:
                return 

            ans = evaluate(node)
            if ans != -1:
                print(node.val, ans)
                res.append(ans)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        res.sort(reverse=True)

        return res[k-1] if len(res) >= k else -1 
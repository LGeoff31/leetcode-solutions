# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        lst = [[root.val]]
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
            a = []
            for node in queue:
                a.append(node.val)
            lst.append(a)
        lst.pop()
        print(lst)
        b = []
        for arr in lst:
            b.append(sum(arr))
        if k > len(lst): return -1
        b.sort(reverse=True)
        return b[k-1]
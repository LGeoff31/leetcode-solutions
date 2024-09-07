# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        @cache
        def dfs(i, treenode):
            if i == len(lst):
                return True
            if not treenode:
                return False
            if treenode.val == lst[i]:
                return dfs(i + 1, treenode.left) or dfs(i + 1, treenode.right) or dfs(0, treenode.left) or dfs(0, treenode.right)
            else:
                return dfs(0, treenode.left) or dfs(0, treenode.right)
            # return False
        return dfs(0, root)
        
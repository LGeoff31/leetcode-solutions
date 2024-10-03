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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next

        print(lst)
        def dfs(l, r):
            if l > r:
                return None
            mid = l + (r-l) // 2
            node = TreeNode(lst[mid])
            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)
            return node
        return dfs(0, len(lst) - 1)



        
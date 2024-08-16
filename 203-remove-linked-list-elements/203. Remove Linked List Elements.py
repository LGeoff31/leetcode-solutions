# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        while curr and curr.val == val:
            curr = curr.next
        if curr is None: return None
        head = curr
        while curr:
            if curr.next and curr.next.val == val:
                nextNode = curr.next
                while nextNode and nextNode.val == val:
                    nextNode = nextNode.next
                curr.next = nextNode
            curr = curr.next
        return head
        
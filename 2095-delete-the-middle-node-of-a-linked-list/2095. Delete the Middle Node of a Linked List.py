# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_size(head):
    if head is None:
        return 0
    return 1 + get_size(head.next)

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        for i in range(get_size(head) // 2):
            prev = curr
            curr = curr.next
        if prev is None:
            return None
        prev.next = curr.next
        return head
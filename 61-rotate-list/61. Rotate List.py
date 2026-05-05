# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        if lst:
            k %= len(lst)
        lst = lst[len(lst) - k : ] + lst[: len(lst) - k]

        new_head = ListNode()
        new_curr = new_head
        for n in lst:
            node = ListNode(n)
            new_curr.next = node
            new_curr = new_curr.next
        return new_head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #size 0-1
        if head is None: return None
        if head.next is None: return head
        #size 2+
        temp = head.next
        currOdd = head
        currEven = head.next
        while currOdd and currEven:
            if currEven and currEven.next is None:
                break
            currOdd.next = currEven.next
            currEven.next = currOdd.next.next
            currOdd = currOdd.next
            currEven = currEven.next
        currOdd.next = temp
        return head
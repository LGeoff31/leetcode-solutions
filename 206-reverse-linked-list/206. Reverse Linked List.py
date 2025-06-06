# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        curr = head
        prev = None

        while curr:
            tmp = curr
            nxtNode = curr.next
            curr.next = prev
            curr = nxtNode
            prev = tmp
        
        return prev
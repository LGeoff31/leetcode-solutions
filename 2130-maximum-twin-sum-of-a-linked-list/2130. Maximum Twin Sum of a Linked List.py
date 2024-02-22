# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        slow, fast = head, head.next
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        
        start = slow.next
        prev = None
        while True:
            nxt = start.next
            start.next = prev
            if nxt is None: break
            prev = start
            start = nxt
        
        while start:
            res = max(res, head.val + start.val)
            head = head.next
            start = start.next
        return res
        
            

        

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(curr):
            size = 0
            while curr:
                size += 1
                curr = curr.next
            return size
        n = length(head)
        if n == 1: return head
        count = 0
        temp = None
        temp2 = None
        curr = head
        while curr:
            if count == k-1:
                temp = curr
            if count == n-k:
                temp2 = curr    
            curr = curr.next
            count += 1
        temp.val, temp2.val = temp2.val, temp.val
        return head
            
        
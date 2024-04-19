# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []    
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        for i in range(0, len(lst)-1, 2):
            lst[i], lst[i+1] = lst[i+1], lst[i]
        res = ListNode()
        curr = res
        for i in range(len(lst)):
            newNode = ListNode(lst[i])
            curr.next = newNode
            curr = curr.next

        return res.next
        
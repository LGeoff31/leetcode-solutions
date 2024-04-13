# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr=curr.next
        a = []
        for i in range(len(lst)): # add all less than x
            if lst[i] < x:
                a.append(lst[i])
        for i in range(len(lst)):
            if lst[i] >= x:
                a.append(lst[i])
        
        res = ListNode()
        curr = res
        for i in range(len(a)):
            newNode = ListNode(a[i])
            curr.next = newNode
            curr = curr.next
        return res.next


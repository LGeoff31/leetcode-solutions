# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        a = head
        curr = head
        start = False
        while curr:
            for i in range(m - 1 + start):
                if not curr:
                    break
                curr = curr.next
            tmp = curr
            if not tmp: 
                print('reached')
                if curr:
                    curr.next = None
                break
            for i in range(n+1):
                if not tmp:
                    curr.next = None
                    break
                tmp = tmp.next
            if not tmp: 
                curr.next = None
                break
            curr.next = tmp
            start = True
        return a
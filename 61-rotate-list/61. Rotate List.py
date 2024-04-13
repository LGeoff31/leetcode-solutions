# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []
        if not head: return None
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        k %= len(lst)

        res = ListNode()
        curr = res
        print(lst)
        for i in range(len(lst) - k, len(lst)):
            newNode = ListNode(lst[i])
            curr.next = newNode
            curr = curr.next

        for i in range(len(lst) - k):
            newNode = ListNode(lst[i])
            curr.next = newNode
            curr = curr.next
        print(res)
        return res.next
        
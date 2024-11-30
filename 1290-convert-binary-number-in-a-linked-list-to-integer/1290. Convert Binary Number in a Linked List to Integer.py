# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        print(length)
        curr = head
        while curr:
            if curr.val == 1:
                res += 2**(length-1)
            length -= 1
            curr = curr.next
        return res


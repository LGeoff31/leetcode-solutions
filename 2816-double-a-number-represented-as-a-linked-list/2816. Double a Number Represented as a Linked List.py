# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        num = 0

        while curr:
            num = 10*num + curr.val
            curr = curr.next
        newVal = num*2 #378
        root = ListNode()
        root.val = sys.set_int_max_str_digits(100000)
        root.val = int(str(newVal)[0]) #3
        cur = root
        for c in str(newVal)[1:]: #78
            z = ListNode()
            z.val = int(c)
            cur.next = z
            cur = cur.next
        return root

        
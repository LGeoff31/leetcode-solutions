# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy  
        carry = 0  
        while l1 or l2 or carry:
            if l1:
                num1 = l1.val
            else:
                num1 = 0
            if l2:
                num2 = l2.val
            else:
                num2 = 0
            val = num1 + num2 + carry
            carry = val // 10
            val %= 10
            curr.next = ListNode(val)

            #update pointers
            curr = curr.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None

        return dummy.next
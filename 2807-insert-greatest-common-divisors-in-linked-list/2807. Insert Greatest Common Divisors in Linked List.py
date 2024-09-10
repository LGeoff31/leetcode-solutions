# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(num1, num2): #O(log(min(a,b)))
            if num2 == 0:
                return num1
            return gcd(num2, num1 % num2)
                
        curr = head
        while curr.next:
            new_node = ListNode(gcd(curr.val, curr.next.val))
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        return head

        
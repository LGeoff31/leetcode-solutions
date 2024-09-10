# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(num1, num2): #O(log(min(a,b)))
            # Use Euclidean Algorithm
            if num1 < num2:
                gcd(num2, num1)
            # num1 will always be larger
            while num2:
                quotient = num1 // num2
                remainder = num1 - num2 * quotient
                num1, num2 = num2, remainder
            return num1
                
        curr = head
        while curr.next:
            new_node = ListNode(gcd(curr.val, curr.next.val))
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        return head

        
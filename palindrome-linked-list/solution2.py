# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next #End of array
            slow = slow.next #Near middle
        
        #Reverse last half of linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        #Check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next
        return True

        
        

        
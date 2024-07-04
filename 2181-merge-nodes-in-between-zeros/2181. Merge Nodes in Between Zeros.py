# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currSum = 0
        res = head.next
        prev = head.next
        curr = head.next
        while curr:
            currSum += curr.val
            if curr.val == 0:
                prev.val = currSum
                prev.next = curr.next
                prev = prev.next
                currSum = 0

            curr = curr.next
        return res


        
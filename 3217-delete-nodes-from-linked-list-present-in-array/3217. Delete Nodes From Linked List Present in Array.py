# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove_nodes = set(nums)
        # Ensure the head if valid
        while head and head.val in remove_nodes:
            head = head.next
        curr = head
        while curr:
            # Check if the next node is not valid
            while curr.next and curr.next.val in remove_nodes:
                curr.next = curr.next.next
            curr = curr.next
        return head
        
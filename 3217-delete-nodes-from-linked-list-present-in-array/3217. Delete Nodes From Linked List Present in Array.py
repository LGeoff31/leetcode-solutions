# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        lst = set(nums)

        a = []
        curr = head
        while curr:
            a.append(curr.val)
            curr = curr.next
        
        b = []
        for elem in a:
            if elem not in lst:
                b.append(elem)
        
        head = ListNode()
        curr_head = head
        for elem in b:
            node = ListNode(elem)
            curr_head.next = node
            curr_head = curr_head.next
        return head.next
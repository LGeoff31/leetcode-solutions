# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        head = ListNode()
        curr = head
        while list1 and list2:
            nxt_node = None
            if list1.val < list2.val:
                nxt_node = ListNode(list1.val)
                list1 = list1.next
            else:
                nxt_node = ListNode(list2.val)
                list2 = list2.next
            
            curr.next = nxt_node
            curr = curr.next

        while list1:
            curr.next = ListNode(list1.val)
            curr = curr.next
            list1 = list1.next

        while list2:
            curr.next = ListNode(list2.val)
            curr = curr.next
            list2 = list2.next

        return head.next
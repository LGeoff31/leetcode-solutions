# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        def linked_list_to_array(head, res):
            if head is None:
                return res
            res.append(head.val)
            return linked_list_to_array(head.next, res)

        def array_to_linked_list(arr):
            if len(arr) == 0:
                return None
            curr = ListNode(arr[0])
            rest = array_to_linked_list(arr[1:])
            curr.next = rest
            return curr

        array = linked_list_to_array(head, [])
        array = array[::-1]
        return array_to_linked_list(array)

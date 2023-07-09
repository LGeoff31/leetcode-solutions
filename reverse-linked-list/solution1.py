# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        def linked_list_to_array(head):
            res = []
            while head is not None:
                res.append(head.val)
                head = head.next
            return res

        def array_to_linked_list(arr):
            nodeA = ListNode(arr[0])
            temp = nodeA
            for i in range(1, len(arr)):
                nodeB = ListNode(arr[i])
                temp.next = nodeB
                temp = nodeB
            return nodeA
        array = linked_list_to_array(head)
        array = array[::-1]
        return array_to_linked_list(array)

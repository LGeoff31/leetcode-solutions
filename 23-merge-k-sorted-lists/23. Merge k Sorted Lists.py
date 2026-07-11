# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = [(linked_list.val, i, linked_list) for i, linked_list in enumerate(lists) if linked_list is not None]
        heapify(minHeap)
        head = ListNode()
        curr = head
        while minHeap:
            node_val, _, node = heappop(minHeap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(minHeap, (node.next.val, _, node.next))
        return head.next

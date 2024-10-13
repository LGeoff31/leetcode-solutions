# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        root = ListNode()
        k = len(lists)
        curr = root

        # Initialize the heap
        for i in range(k):
            if lists[i]:
                heappush(minHeap, (lists[i].val, i, lists[i]))

        # All the pointers must reach the end, all become null
        while minHeap:
            val, idx, node = heappop(minHeap)
            curr.next = node
            curr = curr.next

            if node.next:
                heappush(minHeap, (node.next.val, idx, node.next))
           
        return root.next
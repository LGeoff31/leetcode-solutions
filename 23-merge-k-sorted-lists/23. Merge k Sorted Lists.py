# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, _lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, head in enumerate(_lists):
            if head:
                heappush(minHeap, (head.val, i))
        head = ListNode()
        curr = head
        while minHeap:
            node_val, idx = heappop(minHeap)
            curr.next = _lists[idx]
            _lists[idx] = _lists[idx].next
            if _lists[idx]: 
                heappush(minHeap, (_lists[idx].val, idx))
            curr = curr.next

        return head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        c = count()
        for list_head in lists:
            if list_head:
                heappush(minHeap, (list_head.val, next(c), list_head))
        
        merged_list = ListNode()
        head_list = merged_list
        while minHeap:
            val, _, node = heappop(minHeap)
            merged_list.next = node
            merged_list = merged_list.next

            if node.next:
                heappush(minHeap, (node.next.val, next(c), node.next))

        return head_list.next
        

        
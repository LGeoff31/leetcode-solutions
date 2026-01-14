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
            # print(type(list_head), list_head.val)
            if list_head:
                heappush(minHeap, (list_head.val, next(c), list_head))
        
        merged_list = ListNode()
        head_list = merged_list
        while minHeap:
            val, _, node = heappop(minHeap)
            merged_list.next = node
            merged_list = merged_list.next

            if node.next:
                node = node.next
                heappush(minHeap, (node.val, next(c), node))

        return head_list.next
        

        
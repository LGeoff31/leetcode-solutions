# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def is_critical_point(prev_node, curr, next_node):
            if prev_node is None or next_node is None:
                return False 
            
            return curr.val < min(prev_node.val, next_node.val) or curr.val > max(prev_node.val, next_node.val)

        critical_node_indexes = []
        prev_node = None
        curr = head
        i = 0

        while curr:
            temp = curr
            next_node = curr.next

            if is_critical_point(prev_node, curr, next_node):
                critical_node_indexes.append(i)

            i += 1
            prev_node = temp
            curr = curr.next

        if len(critical_node_indexes) < 2:
            return [-1, -1]
        
        min_distance, max_distance = 1e9, critical_node_indexes[-1] - critical_node_indexes[0]
        for i in range(1, len(critical_node_indexes)):
            prev_idx = critical_node_indexes[i - 1]
            curr_idx = critical_node_indexes[i]
            min_distance = min(min_distance, curr_idx - prev_idx)
        
        return [min_distance, max_distance]
        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        points = []
        for i in range(1, len(lst) - 1):
            if lst[i] > max(lst[i-1], lst[i+1]) or lst[i] < min(lst[i-1], lst[i+1]):
                points.append(i)
        min_dist = 1e9
        if not points:
            return [-1, -1]
        if len(points) == 1:
            return [-1,-1]
        for i in range(1, len(points)):
            min_dist = min(min_dist, points[i] - points[i-1])
        print(points)
        return [min_dist, points[-1] - points[0]]
        
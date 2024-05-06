# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        curr = head

        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        dp = [0] * len(lst)
        dp[-1] = -1
        curr_max = 0
        for i in range(len(lst) - 1, 0, -1):
            curr_max = max(curr_max, lst[i])
            dp[i-1] = curr_max
        
        res = []
        for idx, num in enumerate(lst):
            if num >= dp[idx]:
                res.append(num)
        
        head = ListNode()
        curr = head
        for i in range(len(res)):
            newNode = ListNode(res[i])
            curr.next = newNode
            curr = curr.next
        return head.next
        
        
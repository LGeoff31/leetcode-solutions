# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(res)
        a = 0
        for i in range(len(res) -1, -1, -1):
            if res[i]:
                a += 2 ** (len(res) - i - 1)
        return a
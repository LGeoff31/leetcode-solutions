# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        res = []
        for i in range(0, len(lst), k):
            if i+k <= len(lst):
                for elem in lst[i:i+k][::-1]:
                    res.append(elem)
                # res.append(lst[i:k][::-1])
            else:
                for elem in lst[i:]:
                    res.append(elem)
                # res.append(lst[i:])
        newHead = ListNode()
        newCurr = newHead
        for i in range(len(res)):
            newCurr.next = ListNode(res[i])
            newCurr = newCurr.next

        return newHead.next
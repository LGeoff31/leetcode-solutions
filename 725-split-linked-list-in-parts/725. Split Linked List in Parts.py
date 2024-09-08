# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head: return [None] * k
        def get_size(head):
            size = 0
            while head:
                size += 1
                head = head.next
            return size

        res = []
        size = get_size(head) 
        lst = [size // k] * k
        remainder = size % k
        for i in range(remainder):
            lst[i] += 1
        curr = head
        while curr:
            for elem in lst: #[1, 1, 1, 0, 0]
                if elem == 0:
                    res.append(None)
                    continue
                if not curr:
                    break

                temp_head = curr
                for i in range(elem-1):
                    curr = curr.next
                tmp = curr.next

                curr.next = None
                res.append(temp_head)
                curr = tmp
              

        return res
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        newHead.val = None
        newHead.next = head


        pointer1, pointer2 = head, head

        while pointer1:
            acc = 0
            pointer2 = pointer1
            while pointer2:
                shifted = False
                acc += pointer2.val
                if acc == 0:
                    tempNewHead = newHead
                    while tempNewHead.next != pointer1:
                        tempNewHead = tempNewHead.next
                    tempNewHead.next = pointer2.next
                    print(tempNewHead)
                    print(newHead)
                    pointer1 = tempNewHead.next
                    shifted = True
                    pointer2 = tempNewHead.next
                    acc = 0
                else:
                    pointer2 = pointer2.next
            if not shifted: pointer1 = pointer1.next
        
        return newHead.next
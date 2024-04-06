# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        a = lst[:left-1] + lst[left-1:right][::-1] + lst[right:]
        print(a)
        head = ListNode(a[0])
        b = head
        idx = 1
        while idx < len(a):
            b.next = ListNode(a[idx])
            b=b.next
            idx+=1

        return head
        
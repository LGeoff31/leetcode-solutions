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
        a = []
        for i in range(0, len(lst), k):
            if (i+1) > k * (len(lst) // k):
                for j in range(i, len(lst)):
                    a.append(lst[j])
                break
            subarr = lst[i:i+k][::-1] #size k

            for elem in subarr:
                a.append(elem)

        res = ListNode()
        curr = res
        for i in range(len(a)):
            newNode = ListNode(a[i])
            curr.next = newNode
            curr = curr.next
        return res.next



        return None
        
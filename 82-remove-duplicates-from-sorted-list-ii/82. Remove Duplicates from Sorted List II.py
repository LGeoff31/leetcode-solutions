# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        dic = Counter(lst)
        a=[]
        for key in dic:
            if dic[key] == 1:
                a.append(key)
        a.sort()
        if not a: return None
        print(a)
        res = ListNode(a[0])
        newCurr = res
        for i in range(1, len(a)):
            newNode = ListNode(a[i])
            newCurr.next = newNode
            newCurr = newCurr.next
        return res
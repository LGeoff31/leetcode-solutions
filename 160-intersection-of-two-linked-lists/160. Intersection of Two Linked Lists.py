# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB

        lst1 = []
        lst2 = []

        while currA:
            lst1.append(currA)
            currA = currA.next
        
        while currB:
            lst2.append(currB)
            currB = currB.next
        lst2 = set(lst2)
        for elem in lst1:
            if elem in lst2:
                return elem
        return None
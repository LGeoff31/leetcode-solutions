# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, _lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = []
        for node in _lists:
            a = []
            start = node
            while start:
                a.append(start.val)
                start = start.next 
            lists.append(a)
        def merge(l1, l2):
            lst = []
            p1, p2 = 0, 0
            print(l1, l2)
            while p1 < len(l1) and p2<len(l2):
                if l1[p1] < l2[p2]:
                    lst.append(l1[p1])
                    p1 += 1
                else:
                    lst.append(l2[p2])
                    p2 += 1

            while p1<len(l1):
                lst.append(l1[p1])
                p1 += 1
            while p2<len(l2):
                lst.append(l2[p2])
                p2 += 1
            return lst
        def mergeK(l, r):
            if l < 0 or l >= len(lists):
                return []
            if l == r:
                return lists[l]
            mid = (l+r)//2
            leftMerge = mergeK(l, mid)
            rightMerge = mergeK(mid + 1, r)
            return merge(leftMerge, rightMerge)
        result = mergeK(0, len(lists) - 1)
        res = ListNode()
        curr = res
        for elem in result:
            curr.next = ListNode(elem)
            curr = curr.next
        print(result)
        return res.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        ans = [0] * len(lst)
        stack = [0]
        for i in range(len(lst)):
            if not stack:
                stack.append(lst[i])
            else:
                while stack and lst[i] > lst[stack[-1]]:
                    idx = stack.pop()
                    ans[idx] = lst[i]
                stack.append(i)
        return ans
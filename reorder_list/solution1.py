# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast:
            try:
                fast = fast.next.next
                if fast is None:
                    break
                slow = slow.next
            except:
                break
        fast = slow.next

        # reverse linked list
        prev = None
        while fast:
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp
        # prev -> head

        left = head
        right = prev
        # print("right", left)
        while left != right:
            temp_left = left.next
            left.next = right
            left = temp_left
            if left == right:
                break
            try:
                temp_right = right.next
                right.next = left
                right = temp_right
            except:
                break

        # print("prev", slow.next)

        # now slow will be in the middle

        """
        Do not return anything, modify head in-place instead.
        """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque([root])

        def calc(lst):
            count = 0
            sorted_lst = sorted(lst)
            value_to_index = {value: i for i, value in enumerate(sorted_lst)}  # Map of value to correct index

            for i in range(len(lst)):
                while lst[i] != sorted_lst[i]:  # While the current element is not in the correct position
                    correct_idx = value_to_index[lst[i]]  # Get the index where it should be
                    # Swap the current element with the element at its correct position
                    lst[i], lst[correct_idx] = lst[correct_idx], lst[i]
                    count += 1

            return count

        while queue:
            lst = [node.val for node in queue]
            res += calc(lst)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
        return res
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
        def calc(arr):
            n = len(arr)
            # Create a sorted version of the array with indices
            sorted_arr = sorted([(value, index) for index, value in enumerate(arr)])
            
            # Track visited nodes
            visited = [False] * n
            swaps = 0
            
            for i in range(n):
                # If already visited or already in the correct position, skip
                if visited[i] or sorted_arr[i][1] == i:
                    continue
                
                # Count the size of the cycle
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = sorted_arr[j][1]  # Move to the next node in the cycle
                    cycle_size += 1
                
                # Add (cycle_size - 1) to the swap count
                if cycle_size > 1:
                    swaps += cycle_size - 1
            
            return swaps
        # def calc(lst):
        #     count = 0
        #     sorted_lst = sorted(lst)
        #     for i in range(len(lst)):
        #         expected_idx = sorted_lst.index(lst[i])
        #         if expected_idx != i:
        #             while lst[expected_idx] == lst[i]:
        #                 expected_idx += 1
        #             lst[i], lst[expected_idx] = lst[expected_idx], lst[i]
        #             count += 1
        #     return count

        while queue:
            lst = [node.val for node in queue]
            print(lst)
            count = calc(lst)
            print(count)
            res += count
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
        return res
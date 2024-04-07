"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        curr = root
        queue = deque([curr])

        while queue:
            for i in range(len(queue)):
                a = queue.popleft()
                if a.left: queue.append(a.left)
                if a.right: queue.append(a.right)
            for i in range(len(queue) - 1):
                queue[i].next=queue[i+1]
        return root
        
        
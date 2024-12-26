class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        def dfs(node):
            curr = node
            last = node  # Pointer to the last node in the flattened list
            
            while curr:
                next_node = curr.next  # Store the next pointer
                # If the current node has a child
                if curr.child:
                    # Flatten the child list
                    child_last = dfs(curr.child)
        
                    # Connect current node to the child's head
                    curr.next = curr.child
                    curr.child.prev = curr
                    
                    # Connect the child's last node to the next node
                    if next_node:
                        child_last.next = next_node
                        next_node.prev = child_last
                    
                    # Set the child pointer to null
                    curr.child = None
                    
                    # Update the last pointer
                    last = child_last
                else:
                    last = curr
                
                # Move to the next node
                curr = next_node
            
            return last  # Return the last node in the flattened list
        
        dfs(head)
        return head

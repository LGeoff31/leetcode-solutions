"""
-1e9 -> 5
-1e9 -> 5 
-1e9 -> 5 -> 20
"""

class Node:
    def __init__(self, val, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down

class Skiplist:
    def __init__(self):
        self.head = Node(-1e9)

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            while curr.next and curr.next.val < target:
                curr = curr.next 
            
            if curr.next and curr.next.val == target:
                return True 

            curr = curr.down
        return False

    def coin_flip(self):
        return random.choice(["heads", "tails"])

    def add(self, num: int) -> None:
        curr = self.head
        stack = []

        while curr:
            while curr.next and curr.next.val < num:
                curr = curr.next 

            stack.append(curr) # these are nodes, where we have to update the next poiniter to num
            curr = curr.down

        # Update all the nodes in our stack
        should_promote = True
        down_node = None
        while stack and should_promote:
            node = stack.pop()
            next_node = node.next
            new_node = Node(num, next_node, down_node.next if down_node else None)

            new_node.next = next_node
            node.next = new_node

            down_node = node
            should_promote = self.coin_flip() == "heads"

        if should_promote:
            new_node = Node(num, None, down_node)
            self.head = Node(-1e9, new_node, self.head)

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            while curr.next and curr.next.val < num:
                curr = curr.next
            
            if curr.next and curr.next.val == num:
                curr.next = curr.next.next
                found = True
            
            curr = curr.down
        return found

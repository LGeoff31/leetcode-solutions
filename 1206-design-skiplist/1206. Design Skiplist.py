class Node:
    def __init__(self, val=-1e9):
        self.val = val
        self.next = [None] * 20

class Skiplist:
    def __init__(self):
        self.head = Node()

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(19, -1, -1):
            while curr.next[i] and curr.next[i].val <= target:
                curr = curr.next[i]
        return curr.val == target

    def coin_flip(self):
        return random.choice(["heads", "tails"])

    def add(self, num: int) -> None:
        curr = self.head
        new_node = Node(num)
        update = [None] * 20

        # Get to position where it should be inserted
        for i in range(19, -1, -1):
            while curr.next[i] and curr.next[i].val <= num:
                curr = curr.next[i]
            update[i] = curr
        
        # Insert the node

        next_level = 1
        next_node = curr.next[0]
        curr.next[0] = new_node
        new_node.next[0] = next_node

        while self.coin_flip() == "heads":
            curr = update[next_level]

            new_node.next[next_level] = curr.next[next_level]
            curr.next[next_level] = new_node
            next_level += 1

    def erase(self, num: int) -> bool:
        curr = self.head
        update = [None] * 20

        if self.search(num) == False:
            return False

        # Get to its prev node
        for i in range(19, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        
        # Delete the node
        next_level = 0
        delete_node = curr.next[0]
        while True:
            curr = update[next_level]

            next_node = curr.next[next_level]
            if next_node == delete_node:
                curr.next[next_level] = next_node.next[next_level]
                next_level += 1
            else:
                break
        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
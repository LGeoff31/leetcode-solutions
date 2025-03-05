class Node:
    def __init__(self, value=-1):
        self.value = value
        self.next = None

class Bucket:
    def __init__(self):
        self.head = Node(-1) # X -> 1 -> 2
        
    def exists(self, num):
        curr = self.head
        while curr:
            if curr.value == num:
                return True
            curr = curr.next
        return False

    def add(self, num):
        if not self.head.next:
            self.head.next = Node(num)
            return
        if self.exists(num):
            return
        
        firstNode = self.head.next
        newNode = Node(num)
        self.head.next = newNode
        newNode.next = firstNode

    def remove(self, num):
        if not self.exists(num) or self.head.next is None: 
            return
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.value == num:
                nextNode = curr.next
                prev.next = nextNode
                return 
            curr = curr.next
            prev = prev.next

class MyHashSet:
    def __init__(self):
        self.buckets = [Bucket() for _ in range(769)]

    def hash(self, num):
        return num % 769

    def add(self, key: int) -> None:
        idx = self.hash(key)
        self.buckets[idx].add(key)

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        self.buckets[idx].remove(key)
        
    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        return self.buckets[idx].exists(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
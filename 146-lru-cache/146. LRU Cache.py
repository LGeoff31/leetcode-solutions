class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dictionary = {}
    
    def add(self, node):    
        nextNode = self.head.next
        node.next = nextNode
        node.prev = self.head
        self.head.next = node
        nextNode.prev = node

    def delete(self, node):
        nextNode = node.next
        prevNode = node.prev
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int: 
        if key in self.dictionary:
            resNode = self.dictionary[key]
            ans = resNode.value
            del self.dictionary[key]
            self.delete(resNode)
            self.add(resNode)
            self.dictionary[key] = self.head.next
            return ans
        return -1
        
    def put(self, key: int, value: int) -> None: 
        if key in self.dictionary:
            node = self.dictionary[key]
            del self.dictionary[key]
            self.delete(node)

        if len(self.dictionary) == self.capacity:
            del self.dictionary[self.tail.prev.key]
            self.delete(self.tail.prev)
        self.add(self.Node(key, value))
        self.dictionary[key] = self.head.next

      
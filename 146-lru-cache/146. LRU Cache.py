
class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dictionary = {}
    
    def addNode(self, node):
        nextNode = self.head.next
        node.next = nextNode
        node.prev = self.head
        self.head.next = node
        nextNode.prev = node

    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int: 
        if key in self.dictionary:
            resNode = self.dictionary[key]
            ans = resNode.val
            del self.dictionary[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.dictionary[key] = self.head.next
            return ans

        return -1
        
    def put(self, key: int, value: int) -> None: 
        if key in self.dictionary:
            curr = self.dictionary[key]
            del self.dictionary[key]
            self.deleteNode(curr)
        if len(self.dictionary) == self.capacity:
            del self.dictionary[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        self.addNode(self.Node(key, value))
        self.dictionary[key] = self.head.next

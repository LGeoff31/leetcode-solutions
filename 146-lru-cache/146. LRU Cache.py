class LRUCache:
    class Node:
        def __init__(self, val=None, key=-1):
            self.val = val
            self.next = None
            self.prev = None
            self.key = key

    def __init__(self, capacity: int):
        self.dic = {} # Store a bunch of key : node addresses
        self.head = None
        self.tail = None
        self.capacity = capacity
  
    def add(self, value, key):    
        newNode = self.Node(value, key)
        self.dic[key] = newNode
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        self.tail.next = newNode
        copy = self.tail
        self.tail = self.tail.next
        self.tail.prev = copy 

    def delete(self, node):
        if node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prevNode = node.prev
            nxtNode = node.next
            prevNode.next = nxtNode
            nxtNode.prev = prevNode
        del self.dic[node.key]


    def get(self, key: int) -> int: 
        if key in self.dic:
            node = self.dic[key]
            self.delete(node)
            self.add(node.val, key)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None: 
        if key in self.dic:
            # Update and place at start
            node = self.dic[key]
            self.delete(node)
            self.add(value, key)
        else:
            if self.capacity == len(self.dic):
                self.delete(self.head)
                # We need to add to front
            self.add(value, key)

        

class Node:
    def __init__(self, val=None, nxt=None, key=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = None

class LRUCache:
    """
    Doubly linked list, head (most recently used) -> tail (least recently used)
    Hashmap, key : node
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {} # key: node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int: 
        if key not in self.dic:
            return -1
        
        node = self.dic[key]
        prevNode = node.prev
        nxtNode = node.next
        prevNode.next = nxtNode
        nxtNode.prev = prevNode

        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node


        return node.val
        
    def put(self, key: int, value: int) -> None: 
        if key in self.dic:
            node = self.dic[key]
            node.val = value

            prevNode = node.prev
            nxtNode = node.next
            prevNode.next = nxtNode
            nxtNode.prev = prevNode

            first = self.head.next
            node.prev = self.head
            node.next = first
            self.head.next = node
            first.prev = node
            return

        if len(self.dic) == self.capacity:
            # REMOVE TAIL
            lru = self.tail.prev
            prevLru = lru.prev
            prevLru.next = self.tail
            self.tail.prev = prevLru


            del self.dic[lru.key]
    
        node = Node(key=key, val=value)
        self.dic[key] = node

        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node
        
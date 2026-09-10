class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # map key -> node
        self.cap = capacity

        self.right = Node(0, 0)
        self.left = Node(0, 0)
        self.right.prev, self.left.next = self.left, self.right
        # initiallize linkedlist: left <-> right

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove from cache
            self.remove(self.cache[key])
        elif len(self.cache) >= self.cap:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]
        # insert in cache as MRU
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

    # MRU
    def insert(self, node) -> None:
        prev = self.right.prev
        next = self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    # input node
    def remove(self, node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    

    



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
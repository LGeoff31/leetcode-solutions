class Node:
    def __init__(self, expiryTime):
        self.prev = None
        self.next = None
        self.expiryTime = expiryTime

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.currentSize = 0
        self.timeToLive = timeToLive
        self.mapping = {}
        self.head = None
        self.tail = None

    def _append(self, node):
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def generate(self, tokenId: str, currentTime: int) -> None:
        node = Node(currentTime + self.timeToLive)
        self._append(node)
        self.mapping[tokenId] = node
        self.currentSize += 1

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.mapping or self.mapping[tokenId].expiryTime <= currentTime:
            return

        node = self.mapping[tokenId]
        prevNode, nxtNode = node.prev, node.next
        if prevNode:
            prevNode.next = nxtNode
        else:
            self.head = nxtNode
        if nxtNode:
            nxtNode.prev = prevNode
        else:
            self.tail = prevNode

        newNode = Node(currentTime + self.timeToLive)
        self._append(newNode)
        self.mapping[tokenId] = newNode  # important: update mapping

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.head and self.head.expiryTime <= currentTime:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.currentSize -= 1
        return self.currentSize
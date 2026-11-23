"""
[3, 0, 2, 5, 4]
getProduct(2) -> 20
getProduct(3) -> 40
getProduct(4) -> 


[0, 0, 9]
getProduct(3) -> 0
"""

class ProductOfNumbers:
    def __init__(self):
        self.stream_prefix = []
        self.zero_indexes = []

    def add(self, num: int) -> None:
        if num == 0:
            self.zero_indexes.append(len(self.stream_prefix))

        if not self.stream_prefix or self.stream_prefix[-1] == 0:
            self.stream_prefix.append(num)
            return
        
        self.stream_prefix.append(num * self.stream_prefix[-1])

    def getProduct(self, k: int) -> int:
        
        length = len(self.stream_prefix)
        l, r = length - k, length - 1

        if bisect_left(self.zero_indexes, l) != bisect_right(self.zero_indexes, r):
            return 0

        if k == len(self.stream_prefix):
            return self.stream_prefix[-1]

        if self.stream_prefix[length - k - 1] == 0:
            return self.stream_prefix[-1]

        return int(self.stream_prefix[-1] / self.stream_prefix[length - k - 1])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
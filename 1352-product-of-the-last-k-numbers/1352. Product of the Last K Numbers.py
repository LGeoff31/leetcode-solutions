class ProductOfNumbers:

    def __init__(self):
        self.prefix = []
        self.last_zero_dis = 0

    def add(self, num: int) -> None: # O(1)
        if not self.prefix:
            self.prefix.append(num)
            self.last_zero_dis += num != 0
            return
        if num == 0:
            self.prefix.append(0)
            self.last_zero_dis = 0
        else:
            if self.prefix[-1] == 0:
                self.prefix.append(num)
            else:
                self.prefix.append(num * self.prefix[-1])
            self.last_zero_dis += 1
    def getProduct(self, k: int) -> int: # O(k)
        if k > self.last_zero_dis: return 0
        n = len(self.prefix)
        if len(self.prefix) == k: return self.prefix[-1]
        if self.prefix[n-k-1] == 0:
            return self.prefix[-1]
        return self.prefix[-1] // self.prefix[n-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
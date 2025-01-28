class Allocator:
    def __init__(self, n: int):
        self.n = n
        self.lst = [0] * n
        
    def allocateValues(self, start, end, id):
        for i in range(start, end + 1):
            self.lst[i] = id

    def allocate(self, size: int, mID: int) -> int:
        currFreed = 0
        for i in range(self.n):
            # Sliding window for subarr sweep O(n*size) -> O(n)
            if self.lst[i] == 0:
                currFreed += 1
            else:
                currFreed = 0
            if currFreed >= size:
                # Go from (i-currFreed, i)
                self.allocateValues(i-currFreed+1, i, mID)
                return i-currFreed+1
        return -1

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i in range(self.n):
            if self.lst[i] == mID:
                self.lst[i] = 0
                freed += 1
        return freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
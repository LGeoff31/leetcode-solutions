class Bucket:
    def __init__(self):
        self.bucket = []
    
    def put(self, key, value):
        for i, (k, v) in enumerate(self.bucket):
            if k == key:
                self.bucket[i] = [key, value]
                return
        self.bucket.append([key, value])
        return
    
    def get(self, key):
        for i, (k,v) in enumerate(self.bucket):
            if k == key:
                return v
        return -1

    def remove(self, key):
        for i, (k,v) in enumerate(self.bucket):
            if k == key:
                del self.bucket[i]
        return

class MyHashMap:

    def __init__(self):
        self.MOD = 2069
        self.lst = [Bucket() for i in range(self.MOD)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.MOD
        return self.lst[idx].put(key, value)

    def get(self, key: int) -> int:
        idx = key % self.MOD
        return self.lst[idx].get(key)
        

    def remove(self, key: int) -> None:
        idx = key % self.MOD
        return self.lst[idx].remove(key)
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
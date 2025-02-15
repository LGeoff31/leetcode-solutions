class MRUQueue:
    def __init__(self, n: int):
        self.chunks = []
        self.lst = list(range(1, n+1))
        self.chunksize = ceil(sqrt(n))
        for i in range(0, n, self.chunksize):
            chunk = self.lst[i : i + self.chunksize]
            self.chunks.append(deque(chunk))

    def fetch(self, k: int) -> int:
        k -= 1
        # Find the bucket, and index within bucket
        bucket_idx = k // self.chunksize # 5 // 2 = 2
        remainder = k % self.chunksize # 5 % 2 = 1
        target_num = self.chunks[bucket_idx][remainder]

        # Remove it
        temp = deque()
        for i in range(len(self.chunks[bucket_idx])):
            if i != remainder:
                temp.append(self.chunks[bucket_idx][i])
        self.chunks[bucket_idx] = temp

        # Add it to last bucket
        self.chunks[-1].append(target_num)
                
        # Shift over every element by 1 to the left
        for i in range(bucket_idx, len(self.chunks) - 1): # O(sqrt(len(self.chunks)))
            curr_bucket = self.chunks[i] # Python is referncing this, so this is reference updating curr_bucket updates self.chunks
            next_bucket = self.chunks[i+1]
            curr_bucket.append(next_bucket.popleft())
        return target_num
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
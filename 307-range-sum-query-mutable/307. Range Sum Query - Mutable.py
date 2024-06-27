class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.total = defaultdict(int)
    
    def update(self, o, l, r, idx ,val):
        if l == r:
            self.total[o] = val
            return
        mid = (l+r) // 2
        if idx <= mid:
            self.update(2*o, l, mid, idx, val)
        else:
            self.update(2*o+1, mid+1, r, idx, val)
        self.total[o] = self.total[2*o] + self.total[2*o + 1] # I want self.total[0] to store the sum of that node
        return
    
    def query(self, o, l, r, left, right): 
        # Out of query range
        if r < left or l > right:
            return 0
        
        # Completely inside query range
        if l >= left and r <= right:
            return self.total[o]

        #Partial inside
        mid = (l+r) // 2
        res = 0
        if left <= mid:
            res += self.query(2*o, l, mid, left, right)
        if mid+1 <= right:
            res += self.query(2*o+1, mid+1, r, left, right)
        return res

class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = SegmentTree(self.n)
        self.nums = nums
        for i in range(len(nums)):
            self.tree.update(1, 1, self.n, i+1, nums[i])

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        self.tree.update(1, 1, self.n, index+1, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(1, 1, self.n, left+1, right+1)
        
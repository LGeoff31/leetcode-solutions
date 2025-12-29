class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (self.n+1)

        for i, val in enumerate(self.nums):
            self.updateTree(i+1, val)
        
    def updateTree(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i&-i

    def getSum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i&-i
        return res


    def update(self, index: int, val: int) -> None: #O(1)
        diff = val - self.nums[index]
        self.nums[index] = val
        self.updateTree(index+1, diff)


    def sumRange(self, left: int, right: int) -> int: #O(n)
        return self.getSum(right+1) - self.getSum(left)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.trees = [0] * (2*self.n) # Note that the first element is a blank??????

        # Populate the leaf nodes
        for i in range(self.n):
            self.trees[i+self.n] = nums[i]
        # Populate remainder tree
        for i in range(self.n - 1, 0, -1):
            self.trees[i] = self.trees[2*i] + self.trees[2*i+1]


class NumArray:
    def __init__(self, nums: List[int]):
        self.segmentTree = SegmentTree(nums)
        self.n = len(nums)

    def update(self, index: int, val: int) -> None:
        trees = self.segmentTree.trees
        pos = index + self.n
        trees[pos] = val
        # Update the tree accordingly
        while pos > 1:
            pos //= 2
            trees[pos] = trees[2*pos] + trees[2*pos+1]

    def sumRange(self, left: int, right: int) -> int:   
        res = 0
        left += self.n
        right += self.n
        trees = self.segmentTree.trees
        while left <= right:
            if left % 2 == 1:
                res += trees[left]
                left += 1
            if right % 2 == 0:
                res += trees[right]
                right -= 1
            left //= 2
            right //= 2
        return res


        
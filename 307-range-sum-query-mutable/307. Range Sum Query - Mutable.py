class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.val = 0
        self.left = None #point to attatch next node
        self.right = None

class NumArray:
    def __init__(self, nums: List[int]):
        def createTree(nums, l, r):
            if l > r:
                return None
            
            if l == r:
                n = Node(l, r)
                n.val = nums[r]
                return n

            mid = (l+r) // 2
            root = Node(l, r)

            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            root.val = root.left.val + root.right.val
            return root
        
        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        #recursively get to that leaf node and then recurse upwards to update all the values
        def updateVal(root, i, val):
            if root.start == root.end:
                root.val = val
                return val

            mid = (root.start + root.end) // 2
            if i <= mid: #want to go down left branch
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            root.val = root.left.val + root.right.val
            return root.val
        return updateVal(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def rangeSum(root, left, right):
            if root.start == left and root.end == right:
                return root.val
            
            mid = (root.start + root.end) // 2
            if right <= mid:
                return rangeSum(root.left, left, right)
            elif left >= mid + 1:
                return rangeSum(root.right, left, right)
            else:
                return rangeSum(root.left, left, mid) + rangeSum(root.right, mid+1 ,right)
        return rangeSum(self.root, left, right)
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
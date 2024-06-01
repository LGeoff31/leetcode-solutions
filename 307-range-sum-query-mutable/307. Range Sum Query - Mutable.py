class Node():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.val = 0

class NumArray:
    def __init__(self, nums: List[int]):
        def createTree(nums, l, r):
            if l > r:
                return None
            if l == r:
                node = Node(l, r)
                node.val = nums[l]
                return node
            
            mid = (l+r)//2
            root = Node(l, r)

            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            root.val = root.left.val + root.right.val
            return root

        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def updateVal(node, i, val):
            if node.start == node.end:
                node.val = val
                return val
            mid = (node.start + node.end) // 2
            if i > mid:
                updateVal(node.right, i, val)
            else:
                updateVal(node.left, i, val)
            node.val = node.left.val + node.right.val
            return node.val
        return updateVal(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def rangeSum(node, l, r):
            if node.start == l and node.end == r:
                return node.val
            mid = (node.start + node.end) // 2
            #check if the query range is strictly on the left or right side
            if r <= mid: #strictly on the left
                return rangeSum(node.left, l, r)
            elif l > mid: #strictly on the right
                return rangeSum(node.right,l, r)
            else:
                return rangeSum(node.left, l, mid) + rangeSum(node.right, mid+1, r)
        return rangeSum(self.root, left, right)
                

       
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
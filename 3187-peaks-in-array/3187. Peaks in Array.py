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
        self.total[o] = self.total[2*o] + self.total[2*o + 1]
        return
    
    def query(self, o, l, r, left, right):
        # Out of query range
        if r < left or l > right:
            return 0
        
        # Completely inside query range
        if l >= left and r <= right:
            return self.total[o]
        mid = (l+r) // 2
        res = 0

        if left <= mid:
            res += self.query(2*o, l, mid, left, right)
        if mid+1 <= right:
            res += self.query(2*o+1, mid+1, r, left, right)
        return res


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = SegmentTree(n)

        # Update Initial peak number
        for i in range(1, n-1):
            if nums[i] > max(nums[i-1], nums[i+1]):
                tree.update(1, 1, n, i+1, 1)
        
        res = []
        for a,b,c in queries:
            if a == 1: # Calculate # of peaks from [b, c]
                # Note that elements b and c do not count as peaks so query [b+1, c-1]
                res.append(tree.query(1, 1, n, b+2, c)) # 1 indexed
            else:
                nums[b] = c
                
                # Update the Segment Tree
                if 1 <= b <= n-2: #Only nums[1, n-2] have change be peak
                    if nums[b] > max(nums[b-1], nums[b+1]):
                        tree.update(1, 1, n, b+1, 1) # I guess 1 -> peak
                    else:
                        tree.update(1, 1, n, b+1, 0)
                if b >= 2: #Check nums[i-1] is peak number after change
                    if nums[b-1] > max(nums[b-2], nums[b]):
                        tree.update(1, 1, n, b, 1)
                    else:
                        tree.update(1, 1, n, b, 0)
                if b <= n-3: #Check nums[i+1] is peak number after change
                    if nums[b+1] > max(nums[b+2], nums[b]):
                        tree.update(1, 1, n, b+2, 1)
                    else:
                        tree.update(1, 1, n, b+2, 0)
        return res

        
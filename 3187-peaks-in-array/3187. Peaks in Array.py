class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.total = defaultdict(int)
    def update(self, o, l, r, idx, val):
        if l == r:
            self.total[o] = val
            return
        mid = (l + r) // 2
        if idx <= mid: # Go left side
            self.update(2*o, l, mid, idx, val)
        else: # Go right side
            self.update(2*o+1, mid+1, r, idx, val)
        self.total[o] = self.total[2*o] + self.total[2*o+1]
        return
    
    def query(self, o, l, r, left, right):
        # if l > r:
        #     return 0

        # Completely contained
        if l >= left and r <= right:
            return self.total[o]
        
        # Completely not contained
        if l > right or left > r:
            return 0
        
        # Partially contained
        res = 0
        mid = (l+r) // 2
        if left <= mid:
            res += self.query(2*o, l, mid, left, right)
        if mid+1 <= right:
            res += self.query(2*o+1, mid+1, r, left, right)
        return res


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = SegmentTree(n)
        res = []

        # Initialize segment tree by asseriting any peaks initially
        for i in range(1, n- 1): 
            if nums[i] > max(nums[i-1], nums[i+1]):
                tree.update(1, 1, n, i+1, 1)

        for a,b,c in queries:
            if a == 1:
                res.append(tree.query(1, 1, n, b+2, c))
            else:
                nums[b] = c
                # Only non-boundary elements can become a peak
                if 1 <= b <= n-2:
                    if nums[b] > max(nums[b-1], nums[b+1]):
                        tree.update(1, 1, n, b+1, 1)
                    else:
                        tree.update(1, 1, n, b+1, 0) #O(logn)
                # Maybe left one became peak?
                if b >= 2:
                    if nums[b-1] > max(nums[b-2], nums[b]):
                        tree.update(1, 1, n, b, 1)
                    else:
                        tree.update(1, 1, n, b, 0)
                # Maybe right one became peak?
                if b <= n-3:
                    if nums[b+1] > max(nums[b], nums[b+2]):
                        tree.update(1, 1, n, b+2, 1)
                    else:
                        tree.update(1, 1, n, b+2, 0)
        return res



        